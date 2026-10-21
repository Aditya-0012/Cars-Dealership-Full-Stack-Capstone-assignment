import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from .models import Dealer, DealerReview, CarMake
from .sentiment import analyze_sentiment

def payload(request):
    try:
        return json.loads(request.body.decode('utf-8') or '{}') if 'application/json' in (request.content_type or '') else request.POST
    except (json.JSONDecodeError, UnicodeDecodeError): return None

def home(request):
    state=request.GET.get('state','').strip()
    dealers=Dealer.objects.all()
    if state: dealers=dealers.filter(state__iexact=state)
    states=Dealer.objects.order_by('state').values_list('state',flat=True).distinct()
    return render(request,'dealership/home.html',{'dealers':dealers,'states':states,'selected_state':state})

def dealer_detail(request,dealer_id):
    dealer=get_object_or_404(Dealer,pk=dealer_id)
    return render(request,'dealership/dealer_detail.html',{'dealer':dealer,'reviews':dealer.reviews.select_related('user')})

def login_page(request):
    if request.user.is_authenticated: return redirect('home')
    return render(request,'dealership/login.html')

def review_page(request,dealer_id):
    dealer=get_object_or_404(Dealer,pk=dealer_id)
    if not request.user.is_authenticated: return redirect(f'/login/?next=/dealer/{dealer.pk}/review/')
    return render(request,'dealership/review_form.html',{'dealer':dealer})

@require_GET
def list_dealers(request):
    dealers=Dealer.objects.all()
    state=request.GET.get('state') or request.GET.get('State')
    if state: dealers=dealers.filter(state__iexact=state.strip())
    return JsonResponse({'dealers':[d.as_dict() for d in dealers],'count':dealers.count()})

@require_GET
def get_dealer(request,dealer_id):
    d=get_object_or_404(Dealer,pk=dealer_id)
    return JsonResponse({'dealer':d.as_dict()})

@require_GET
def get_reviews(request,dealer_id):
    d=get_object_or_404(Dealer,pk=dealer_id)
    reviews=[r.as_dict() for r in d.reviews.select_related('user')]
    return JsonResponse({'dealer_id':d.pk,'dealer':d.name,'reviews':reviews,'count':len(reviews)})

@csrf_exempt
@require_POST
def register_user(request):
    data=payload(request)
    if data is None: return JsonResponse({'error':'Invalid JSON'},status=400)
    username=str(data.get('username','')).strip(); password=str(data.get('password',''))
    first=str(data.get('first_name','')).strip(); last=str(data.get('last_name','')).strip(); email=str(data.get('email','')).strip()
    if not all([username,password,first,last,email]): return JsonResponse({'error':'All five fields are required.'},status=400)
    if User.objects.filter(username=username).exists(): return JsonResponse({'error':'Username already exists.'},status=409)
    if User.objects.filter(email=email).exists(): return JsonResponse({'error':'Email already exists.'},status=409)
    user=User.objects.create_user(username=username,password=password,first_name=first,last_name=last,email=email)
    return JsonResponse({'message':'Registration successful.','username':user.username},status=201)

@csrf_exempt
@require_POST
def login_user(request):
    data=payload(request)
    if data is None: return JsonResponse({'error':'Invalid JSON'},status=400)
    user=authenticate(request,username=str(data.get('username','')).strip(),password=str(data.get('password','')))
    if user is None: return JsonResponse({'error':'Invalid username or password.'},status=401)
    login(request,user)
    return JsonResponse({'message':'Login successful.','username':user.username})

@csrf_exempt
@require_POST
def logout_user(request):
    was=request.user.is_authenticated
    logout(request)
    return JsonResponse({'message':'Logout successful.','was_authenticated':was})

@csrf_exempt
@require_POST
def create_review(request):
    if not request.user.is_authenticated: return JsonResponse({'error':'Authentication required.'},status=401)
    data=payload(request)
    if data is None: return JsonResponse({'error':'Invalid JSON'},status=400)
    try: dealer=Dealer.objects.get(pk=int(data.get('dealer_id',0))); rating=int(data.get('rating',5)); text=str(data.get('review','')).strip()
    except (Dealer.DoesNotExist,TypeError,ValueError): return JsonResponse({'error':'A valid dealer_id is required.'},status=400)
    if not 1<=rating<=5 or not text: return JsonResponse({'error':'Review text and a rating from 1 to 5 are required.'},status=400)
    review=DealerReview.objects.create(dealer=dealer,user=request.user,rating=rating,review=text,sentiment=analyze_sentiment(text)['sentiment'])
    return JsonResponse({'message':'Review posted successfully.','review':review.as_dict()},status=201)

@require_GET
def list_car_makes(request):
    makes=[m.as_dict() for m in CarMake.objects.all()]
    return JsonResponse({'car_makes':makes,'count':len(makes)})

@csrf_exempt
@require_POST
def analyze_review(request):
    data=payload(request)
    if data is None: return JsonResponse({'error':'Invalid JSON'},status=400)
    text=str(data.get('review',data.get('text',''))).strip()
    if not text: return JsonResponse({'error':'Review text is required.'},status=400)
    return JsonResponse({'review':text,**analyze_sentiment(text)})

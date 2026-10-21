from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views
urlpatterns=[
 path('',views.home,name='home'),
 path('about/',RedirectView.as_view(url='/static/About.html',permanent=False),name='about'),
 path('contact/',RedirectView.as_view(url='/static/Contact.html',permanent=False),name='contact'),
 path('login/',views.login_page,name='login'),
 path('dealer/<int:dealer_id>/',views.dealer_detail,name='dealer_detail'),
 path('dealer/<int:dealer_id>/review/',views.review_page,name='review_page'),
 path('djangoapp/api/dealers/',views.list_dealers,name='api_dealers'),
 path('djangoapp/api/dealers/<int:dealer_id>/',views.get_dealer,name='api_dealer'),
 path('djangoapp/api/dealers/<int:dealer_id>/reviews/',views.get_reviews,name='api_reviews'),
 path('djangoapp/api/register/',views.register_user,name='api_register'),
 path('djangoapp/api/login/',views.login_user,name='api_login'),
 path('djangoapp/api/logout/',views.logout_user,name='api_logout'),
 path('djangoapp/api/reviews/',views.create_review,name='api_create_review'),
 path('djangoapp/api/car-makes/',views.list_car_makes,name='api_car_makes'),
 path('djangoapp/api/analyze-review/',views.analyze_review,name='api_analyze_review'),
]

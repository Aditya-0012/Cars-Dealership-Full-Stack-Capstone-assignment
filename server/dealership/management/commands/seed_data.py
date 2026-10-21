import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from dealership.models import Dealer, DealerReview, CarMake
DEALERS=[
('Prairie Motor Group','Wichita','Kansas','1200 E Central Ave, Wichita, KS','+1-316-555-0101','wichita@prairiemotors.example'),
('Sunflower Auto House','Topeka','Kansas','2500 SW Topeka Blvd, Topeka, KS','+1-785-555-0102','topeka@sunflowerauto.example'),
('Crossroads Car Center','Overland Park','Kansas','8900 Metcalf Ave, Overland Park, KS','+1-913-555-0103','sales@crossroadscars.example'),
('Lone Star Automotive','Austin','Texas','700 Congress Ave, Austin, TX','+1-512-555-0104','hello@lonestarauto.example'),
('Golden Gate Motors','San Jose','California','1500 Story Rd, San Jose, CA','+1-408-555-0105','team@goldengatemotors.example'),
('Lakeview Auto Gallery','Chicago','Illinois','6400 N Lincoln Ave, Chicago, IL','+1-773-555-0106','info@lakeviewauto.example'),
('Empire State Cars','Albany','New York','90 Central Ave, Albany, NY','+1-518-555-0107','sales@empirecars.example'),
('Rocky Mountain Auto','Denver','Colorado','1800 W Colfax Ave, Denver, CO','+1-303-555-0108','contact@rockymountainauto.example')]
PHOTO='https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1200&q=80'
MAKES=[('Audi','A4'),('Audi','Q5'),('BMW','3 Series'),('BMW','X5'),('Chevrolet','Equinox'),('Ford','F-150'),('Ford','Mustang'),('Honda','Accord'),('Honda','CR-V'),('Hyundai','Tucson'),('Kia','Sportage'),('Mercedes-Benz','C-Class'),('Nissan','Altima'),('Subaru','Outback'),('Tesla','Model 3'),('Toyota','Camry'),('Toyota','RAV4'),('Volkswagen','Jetta')]
class Command(BaseCommand):
    help='Load illustrative dealer data and a demo login account.'
    def handle(self,*args,**kwargs):
        for name,city,state,address,phone,email in DEALERS:
            Dealer.objects.update_or_create(name=name,defaults={'city':city,'state':state,'address':address,'phone':phone,'email':email,'website':'https://example.com','image_url':PHOTO})
        for make,model in MAKES: CarMake.objects.get_or_create(make=make,model=model,year=2025)
        user=None
        if os.environ.get('CREATE_DEMO_USER','').lower() == 'true':
            user,created=User.objects.get_or_create(username='demo',defaults={'email':'demo@example.com','first_name':'Demo','last_name':'User'})
            user.set_password(os.environ['DEMO_USER_PASSWORD'])
            user.save()
        d=Dealer.objects.order_by('id').first()
        if user and d and not d.reviews.exists(): DealerReview.objects.create(dealer=d,user=user,rating=5,review='Fantastic services and a friendly team.',sentiment='positive')
        user_status='demo user available for this run' if user else 'demo user disabled by default'
        self.stdout.write(self.style.SUCCESS(f'Seed complete: {Dealer.objects.count()} dealers, {CarMake.objects.count()} car models; {user_status}.'))

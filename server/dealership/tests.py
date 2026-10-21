import json
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Dealer, CarMake
class DealershipApiTests(TestCase):
    def setUp(self):
        self.dealer=Dealer.objects.create(name='Test Dealer',city='Wichita',state='Kansas',address='1 Main St',phone='555-0100',email='test@example.com')
        User.objects.create_user(username='testuser',password='TestPass123!')
        CarMake.objects.create(make='Toyota',model='Camry',year=2025)
    def test_dealers_endpoint_lists_dealers(self):
        response=self.client.get('/djangoapp/api/dealers/')
        self.assertEqual(response.status_code,200); self.assertEqual(response.json()['count'],1)
    def test_state_filter(self):
        response=self.client.get('/djangoapp/api/dealers/?state=Kansas')
        self.assertEqual(response.status_code,200); self.assertEqual(response.json()['count'],1)
    def test_login_and_logout(self):
        response=self.client.post('/djangoapp/api/login/',data=json.dumps({'username':'testuser','password':'TestPass123!'}),content_type='application/json')
        self.assertEqual(response.status_code,200); self.assertEqual(response.json()['username'],'testuser')
        logout=self.client.post('/djangoapp/api/logout/',data='{}',content_type='application/json')
        self.assertEqual(logout.status_code,200)
    def test_sentiment_fantastic_services(self):
        response=self.client.post('/djangoapp/api/analyze-review/',data=json.dumps({'review':'Fantastic services'}),content_type='application/json')
        self.assertEqual(response.status_code,200); self.assertEqual(response.json()['sentiment'],'positive')
    def test_review_requires_login(self):
        response=self.client.post('/djangoapp/api/reviews/',data=json.dumps({'dealer_id':self.dealer.pk,'rating':5,'review':'Excellent'}),content_type='application/json')
        self.assertEqual(response.status_code,401)

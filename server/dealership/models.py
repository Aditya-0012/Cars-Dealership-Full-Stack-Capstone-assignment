from django.conf import settings
from django.db import models
class Dealer(models.Model):
    name=models.CharField(max_length=160)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100,db_index=True)
    address=models.CharField(max_length=240)
    phone=models.CharField(max_length=40)
    email=models.EmailField()
    website=models.URLField(blank=True)
    image_url=models.URLField(blank=True)
    class Meta: ordering=['state','city','name']
    def __str__(self): return f'{self.name} — {self.city}, {self.state}'
    def as_dict(self): return {'id':self.pk,'name':self.name,'city':self.city,'state':self.state,'address':self.address,'phone':self.phone,'email':self.email,'website':self.website,'image_url':self.image_url}
class DealerReview(models.Model):
    dealer=models.ForeignKey(Dealer,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='dealer_reviews')
    rating=models.PositiveSmallIntegerField(default=5)
    review=models.TextField(max_length=1500)
    sentiment=models.CharField(max_length=16,default='neutral')
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta: ordering=['-created_at']
    def __str__(self): return f'{self.dealer.name} review by {self.user.username}'
    def as_dict(self): return {'id':self.pk,'dealer_id':self.dealer_id,'username':self.user.username,'rating':self.rating,'review':self.review,'sentiment':self.sentiment,'created_at':self.created_at.isoformat()}
class CarMake(models.Model):
    make=models.CharField(max_length=80,db_index=True)
    model=models.CharField(max_length=80)
    year=models.PositiveSmallIntegerField(default=2025)
    class Meta:
        ordering=['make','model','year']
        unique_together=[('make','model','year')]
    def as_dict(self): return {'id':self.pk,'make':self.make,'model':self.model,'year':self.year}

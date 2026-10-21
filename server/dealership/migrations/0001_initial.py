from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial=True
    dependencies=[migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations=[
        migrations.CreateModel(name='CarMake',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('make',models.CharField(db_index=True,max_length=80)),('model',models.CharField(max_length=80)),('year',models.PositiveSmallIntegerField(default=2025))],options={'ordering':['make','model','year'],'unique_together':{('make','model','year')}}),
        migrations.CreateModel(name='Dealer',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('name',models.CharField(max_length=160)),('city',models.CharField(max_length=100)),('state',models.CharField(db_index=True,max_length=100)),('address',models.CharField(max_length=240)),('phone',models.CharField(max_length=40)),('email',models.EmailField(max_length=254)),('website',models.URLField(blank=True)),('image_url',models.URLField(blank=True))],options={'ordering':['state','city','name']}),
        migrations.CreateModel(name='DealerReview',fields=[('id',models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name='ID')),('rating',models.PositiveSmallIntegerField(default=5)),('review',models.TextField(max_length=1500)),('sentiment',models.CharField(default='neutral',max_length=16)),('created_at',models.DateTimeField(auto_now_add=True)),('dealer',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='reviews',to='dealership.dealer')),('user',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name='dealer_reviews',to=settings.AUTH_USER_MODEL))],options={'ordering':['-created_at']})
    ]

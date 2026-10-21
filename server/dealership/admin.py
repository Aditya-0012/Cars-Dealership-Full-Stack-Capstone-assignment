from django.contrib import admin
from .models import Dealer, DealerReview, CarMake
@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display=('name','city','state','phone'); search_fields=('name','city','state'); list_filter=('state',)
@admin.register(DealerReview)
class ReviewAdmin(admin.ModelAdmin):
    list_display=('dealer','user','rating','sentiment','created_at'); list_filter=('rating','sentiment')
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin): list_display=('make','model','year'); list_filter=('make','year')

from django.contrib import admin
from .models import Seller, Pineapple, Order, Comment, Subscription
# Register your models here.

admin.site.register(Seller)
admin.site.register(Pineapple)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(Subscription)

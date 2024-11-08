from django.contrib import admin
from .models import *


#this is visible in the admin panel of the website (django admin)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


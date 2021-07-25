from django.contrib import admin
from .models import Order, Product, Promotion, ProductPromotion, VendorCommisions, OrderLine

admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Promotion)
admin.site.register(ProductPromotion)
admin.site.register(VendorCommisions)
admin.site.register(OrderLine)

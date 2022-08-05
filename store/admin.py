from django.contrib import admin
from .models import (
    Address,
    Cart,
    CartItem,
    Collection,
    Customer,
    Order,
    OrderItem,
    Product,
    Promotion,
)

# Register your models here.

admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Collection)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Promotion)

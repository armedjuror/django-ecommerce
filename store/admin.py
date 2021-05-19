from django.contrib import admin
from django.contrib.auth.models import User
from .models import (
    Address,
    Product,
    ProductImage,
    Order,
    OrderItem
)


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
    ]


class UserAddressInline(admin.StackedInline):
    model = Address


class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserAddressInline
    ]


class ProductImageInline(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

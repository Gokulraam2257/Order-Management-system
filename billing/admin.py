from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from billing.models import Products, customer, Order, Order_detail

# Register your models here.


class MyAdminSite(AdminSite):
    def each_context(self, request):
        context = super(MyAdminSite, self).each_context(request)

        return {'username': request.user}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass


@admin.register(Order_detail)
class Order_detailAdmin(admin.ModelAdmin):
    pass


@admin.register(customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("f_name", "l_name")
    pass


@admin.register(Order)
class orderAdmin(admin.ModelAdmin):
    pass

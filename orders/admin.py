from django.contrib import admin

from .models import Order, Product, RefundRequest


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "in_stock")


class OderAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "product_name",
        "amount",
        "status",
        "carrier",
        "tracking_number",
    )


class RefundAdmin(admin.ModelAdmin):
    list_display = ("order", "user", "reason", "status")


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OderAdmin)
admin.site.register(RefundRequest, RefundAdmin)

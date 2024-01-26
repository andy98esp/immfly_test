"""from django.contrib import admin

from application.models import (
    ShopifyCustomerModel,
)


class ShopifyCustomerAdmin(admin.ModelAdmin):
    readonly_fields = ('instance_created_at', 'instance_updated_at',)


admin.site.register(ShopifyCustomerModel, ShopifyCustomerAdmin)
"""

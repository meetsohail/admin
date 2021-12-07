from django.contrib import admin
from .models import Product
import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SEC_KEY


class ProductAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        if not obj.product_stripe_id and not obj.product_stripe_price_id:
            stripe_product = stripe.Product.create(
                name=obj.product_name,
                active=obj.product_status,
                description=obj.product_description
            )
            price = int(obj.product_price) * 100
            stripe_price = stripe.Price.create(
                unit_amount=price,
                currency="usd",
                recurring={"interval": "month"},
                product=stripe_product.id,
            )
            obj.product_stripe_id = stripe_product.id
            obj.product_stripe_price_id = stripe_price.id
        super(ProductAdmin, self).save_model(request, obj, form, change)
        
admin.site.register(Product, ProductAdmin)
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', views.ProductViewSet)

app_name = 'billing'
urlpatterns = [
    path('remove-card/', views.remove_paymentmethod, name='remove-card'),
    path('setup-intent/', views.setup_intent, name='setupintent'),
    path('payment-method/', views.save_payment_method, name='savepaymentmethod'),
    path('stripe-webhooks/', views.stripe_webhooks, name='webhooks'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('switch/', views.switch_subscription, name='switch_subscription'),
    path('get_subscribe/', views.get_subscribe, name='get_subscribe'),
    path('', include(router.urls))
]
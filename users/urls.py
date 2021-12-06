from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'analytics', views.LogViewSet)
router.register(r'invoices', views.InvoiceViewSet)
router.register(r'', views.UserViewSet)

app_name = 'users'
urlpatterns = [
    path('user/', views.authenticated_user, name='user'),
    path('api-key/', views.get_api_key, name='apikey'),
    path('reset-api-key/', views.reset_api_key, name='resetkey'),
    path('analytics-summary/', views.analytics_summary, name='analytics_summary'),
    path('<int:id>/update-settings/', views.update_settings, name='update_settings'),
    path('', include(router.urls))
]
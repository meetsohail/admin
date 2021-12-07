from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views


app_name='dashboard'
urlpatterns=[
    path('logout/', views.logout_view, name='logout'),
    re_path('^.*$', login_required(TemplateView.as_view(template_name='authentication/layouts/spa.html')), name='home')
]
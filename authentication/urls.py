from django.urls import path, re_path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test
from django.conf import settings

passestest = user_passes_test(lambda user: user.is_anonymous, login_url=settings.LOGIN_REDIRECT_URL, redirect_field_name=None)

app_name='authentication'
urlpatterns = [
    path('do-login/', views.login_view, name='login'),
    path('do-register/', views.register_view, name='register'),
    path('do-reset-password/', views.reset_view, name='reset'),
    path('do-update-password/', views.update_pass_view, name='updatepass'),
    re_path('^.*$', passestest(TemplateView.as_view(template_name='authetication/layouts/auth-master.html')), name='spa')
]
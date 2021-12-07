from django.shortcuts import render
from django.contrib.auth import logout
from django.http import JsonResponse


def logout_view(request):
    if request.is_ajax():
        logout(request)
        return JsonResponse({
            'status': True
        })
    else:
        return JsonResponse({
            'status': False
        }, status=400)
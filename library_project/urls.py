"""
URL configuration for library_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path
from django.http import JsonResponse
import sys


urlpatterns = [
    path('admin/', admin.site.urls),
     path('api/', include('src.routers')),
]



def error_404(request,exception=None):
    message=('The endpoint is not found')
    response = JsonResponse(data={'status_code': 404, 'message': message })
    return response


def error_500(request):
    type_, value, traceback = sys.exc_info()
    message=(f'Server Error: {str(value)}')
    print(type_)        
    print(f'value{value}')
    print(traceback)
    response = JsonResponse(data={'status_code': 500, 'message': message })
    return response



handler404= error_404
handler500= error_500

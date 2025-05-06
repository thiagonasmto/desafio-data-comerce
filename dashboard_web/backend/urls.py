"""
URL configuration for seu_bone project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from .views import home_view, UploadCSVView, gerar_top_3_exportados

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('upload-csv/', UploadCSVView.as_view(), name='upload-csv'),
    path('top-3-exportados/', gerar_top_3_exportados, name='top_3_exportados'),
]

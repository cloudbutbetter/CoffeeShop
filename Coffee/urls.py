"""
URL configuration for Coffee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
# for .html url
from shop.views import home,menu,add,delete,manage,order,edit,customer,delete0
# for uplaoding images
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('home/',home,name='home'),
    path('menu/',menu,name='menu'),



    path('manage/',manage,name='manage'),

    path('add/',add,name='add'),
    path('edit/<int:pk>/',edit,name='edit'),
    path('delete/<int:pk>/',delete,name='delete'),
    path('delete0/<int:pk>/',delete0,name='delete0'),



    path('customer/',customer,name='customer'),

    path('order/<int:pk>/',order,name='order'),






]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

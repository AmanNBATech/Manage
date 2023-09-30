"""sites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from shops import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('sign/',views.sign,name='sign'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('enquiry',views.enquiry,name='enquiry'),
    path('contact/',views.contact,name='contact'),
    path('room/',views.room,name='room'),
    path('bk/<int:id>',views.bk,name='bk'),
    path('ins/',views.ins,name='ins'), 
    path('book_room/<int:id>',views.book_room,name='book_room'), 
    path('team/',views.team,name='team'),
    path('service/',views.service,name='service'),
    path('about/',views.about,name='about'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('home/',views.home,name='home'),
    path('bookin/',views.bookin,name='bookin'),
    path('abc/',views.abc,name='abc'),




    
  


]+static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)

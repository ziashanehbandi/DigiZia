"""DigiZia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from DigiZiaApp.views import *
from DigiZiaApp.view2 import *
from django.conf.urls.static import static,settings

urlpatterns = [
    path('admin/', admin.site.urls),

    #auth
    path('signup/', SignUpUser, name="SignUpUser" ),
    path('login/', LoginUser, name="LoginUser" ),
    path('logout/', LogOutUser, name="LogOutUser" ),

    #product
    path('into/<str:digi_pk>', product, name="product"),
    # path('into/phone', phone_product, name="phone_product"),
    path('into/<str:digi_pk>/<str:brand_pk>', each_brand, name="each_brand"),

    #DigiZia
    path('into/', into, name="into"),
    path('', home, name="home"),

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from user import views as user_api
from swiper import views as swiper_api
from vip import views as vip_api

urlpatterns = [
    url(r'^user/verify_code', user_api.get_verify_code),
    url(r'^user/login', user_api.login),
    url(r'^user/get_profile', user_api.get_profile),
    url(r'^user/modify_profile', user_api.modify_profile),

    url(r'^swiper/users', swiper_api.users),
    url(r'^swiper/like', swiper_api.like),
    url(r'^swiper/superlike', swiper_api.superlike),
    url(r'^swiper/dislike', swiper_api.dislike),
    url(r'^swiper/rewind', swiper_api.rewind),
    url(r'^swiper/friends', swiper_api.friends),
    url(r'^vip/modify_vip', vip_api.modify_vip),
    url(r'^vip/get_vip', vip_api.get_vip),
]

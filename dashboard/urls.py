"""ava - dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

<<<<<<< Updated upstream
from dashboard.views import Dashboard, Respond, Sruthi, Neha, Angelica, Vidhya, Register, UserProfileView, Login,Pantry,getRecipe


=======
from dashboard.views import Dashboard, Controller, Sruthi, Neha, Angelica, Vidhya, Register
>>>>>>> Stashed changes

urlpatterns = [
    url(r'^$', Dashboard.as_view(), name='dashboard'),
    url(r'^respond/$', Controller.as_view(), name='controller'),
    url(r'^sruthi/$', Sruthi.as_view(), name='sruthi'),
    url(r'^neha/$', Neha.as_view(), name='neha'),
    url(r'^vidhya/$', Vidhya.as_view(), name='vidhya'),
    url(r'^angelica/$', Angelica.as_view(), name='angelica'),
    url(r'^register/$', Register.as_view(), name='register'),

    url(r'^userprofileview/$', UserProfileView.as_view(), name='profile'),
    url(r'^login/$', Login.as_view(), name='login'),

    url(r'^pantry/$', Pantry.as_view(), name='pantry'),

    url(r'^getrecipe/$', getRecipe.as_view(), name='getrecipe')
]

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

"""import patterns as patterns"""
from django.conf.urls import url, include
from django.contrib import admin


from dashboard.views import Dashboard, UserSignup, RecipeAdmin, Recipe, UserProfileView, Login, Pantry, getRecipe, \
    MainController, UserProfile, AvaRecipe


urlpatterns = [
    url(r'^$', Dashboard.as_view(), name='dashboard'),

    url(r'^userprofileview/$', UserProfileView.as_view(), name='profile'),

    url(r'^login/$', Login.as_view(), name='login'),

    url(r'^pantry/$', Pantry.as_view(), name='pantry'),

    url(r'^getrecipe/$', getRecipe.as_view(), name='getrecipe'),

    url(r'^query/$', MainController.as_view(), name='main_controller'),

    url(r'^ava-admin/$', RecipeAdmin.as_view(), name='recipe_add'),

    url(r'^signup/$', UserSignup.as_view(), name='signup'),

    url(r'^user-profile/(?P<user_id>[0-9]+)/$', UserProfile.as_view(), name='user_profile'),

    url(r'^ava-recipe/$', AvaRecipe.as_view(), name='recipe'),

    url(r'^recipe-admin/$', RecipeAdmin.as_view(), name='recipe_add')

    # url(r'^<slug>$',TemplateLoader.as_view(), name='template_loader')
]
"""
URL configuration for mysiteProject project.

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
from django.urls import path
from homepage.views import home_view, iceland_view, norway_view, winter_view, coversvol1_view, intheautumnforest_view

urlpatterns = [
    path('', home_view, name='home'), #home
    path('iceland/', iceland_view, name='iceland'),
    path('norway/', norway_view, name='norway'),
    path('winter/', winter_view, name='winter'),
    path('covers_vol_1/', coversvol1_view, name='coversvol1'),
    path('in_the_autumn_forest/', intheautumnforest_view, name='intheautuhmforest'),
    path('admin/', admin.site.urls),
]

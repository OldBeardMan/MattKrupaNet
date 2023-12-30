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
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from homepage.views import home_view, iceland_view, norway_view, winter_view, coversvol1_view, intheautumnforest_view, bc_view

urlpatterns = [
    path('', home_view, name='home'), #home
    path('iceland/', iceland_view, name='iceland'),
    path('norway/', norway_view, name='norway'),
    path('winter/', winter_view, name='winter'),
    path('coversvol1/', coversvol1_view, name='coversvol1'),
    path('intheautumnforest/', intheautumnforest_view, name='intheautumnforest'),
    path('bc/', bc_view, name='bc'),
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


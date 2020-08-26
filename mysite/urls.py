"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import os
from django.views.static import serve
from django.conf import settings    
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/polls/', include('polls.urls')),
    path('/hello/', include('home.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('autos/', include('autos.urls')),
    path('cats/', include('cats.urls')),
    path('ads/', include('ads.urls')),

    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    
]

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
           'show_indexes': True},
        name='site_path'
    ),
]

urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
        path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
    )
    print('Using',social_login,'as the login template')
except:
    print('Using registration/login.html as the login template')

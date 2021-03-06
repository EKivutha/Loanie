"""lms URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from material.frontend import urls as frontend_urls
from django.conf.urls.static import static
from django.urls import path

app_name="main"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	
	#matchess /account/****
	url(r'^account/', include('accounts.urls')),
	
	#matches /dashboard/****

    url(r'', include('client.urls')),
    #url(r'^admindash', include('adashboard.urls')),
    url(r'^auth/', include('authentication.urls')),
    url(r'', include(frontend_urls)),
             # Django admin route
    url(r'',  include("authentication.urls")), # Auth routes - login / register
    url(r'^dashboard/',  include("adashboard.urls"))
    
]

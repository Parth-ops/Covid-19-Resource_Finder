"""cov URL Configuration

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
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path,include
from account.views import loginPageS,loginPageB,homes,homeB,registerPageS,registerPageB,intro, ViewS, addButton


urlpatterns = [
    path('admin/', admin.site.urls),
    path('registers/',registerPageS,name='registers'),
    path('registerb/',registerPageB,name='registerb'),
    path('logins/',loginPageS,name='logins'),
    path('loginb/',loginPageB,name='loginb'),
    path('homes/',homes, name="homes"),
    path('homeb/',homeB,name="homeb"),
    path('',intro,name="home"),
    path('ViewS/', ViewS, name="ViewS"),
    path('^addButton', addButton, name='script')
]
urlpatterns +=staticfiles_urlpatterns()

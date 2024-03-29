"""portfolio URL Configuration

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
from django.urls import path
from .views import IndexView, AboutView, BlogView, ContactView, FinderrView, PriceView, ServiceView, PriceView, ProjectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('blog', BlogView.as_view(), name='blog'),
    path('contact', ContactView.as_view(), name='contact'),
    path('finderr', FinderrView.as_view(), name='finderr'),
    path('price', PriceView.as_view(), name='price'),
    path('service', ServiceView.as_view(), name='service'),
    path('project', ProjectView.as_view(), name='project'),
]

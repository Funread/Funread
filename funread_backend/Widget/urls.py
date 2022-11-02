"""Widget URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from rest_framework import routers
from .api import WidgetViewSet
from Widget import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns=[
    
    path('searchwidget/<str:widgetid>', views.widgetSearch),
    path('changewidget/', views.widgetChange),
    path('listwidget/', views.listedWidget),
    path('new-widget/', views.new_widget),
    path('searchwidgetitem/<str:widgetitemid>', views.widgetItemSearch),
    path('changewidgetitem/', views.widgetItemChange),
    path('listwidgetitem/', views.listedWidgetItems),
    path('new-widgetitem/', views.new_widgetItem)
]
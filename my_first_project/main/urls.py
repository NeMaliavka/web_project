from . import views
from django.urls import path

urlpatterns = [
    path('', views.index), #itproger
    path('about', views.about),
    path('crm', views.crm)
]

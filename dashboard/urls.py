from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='Index'),
    path('index', views.index, name='Index'),
    path('AddProducts', views.AddProducts, name='Product'),
    path('ViewProducts', views.ViewProducts, name='Products'),
]
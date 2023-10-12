from django.urls import path
from . import views



# URLs / Routes for endpoints

urlpatterns = [
    
    path('addInventory/', views.addStock),
    path('addSection/', views.addSection),
    path('addProducts/', views.addProduct),
    path('getSections/', views.getSections),
    path('getProducts/', views.getProducts),
    path('getInventory/', views.getInventory),
    path('getSection/<str:pk>/', views.getSection),
    path('getProduct/<str:pk>/', views.getProduct),
    path('getInventory/<str:pk>/', views.getInventory),
    path('dispatchProduct/<str:pk>/', views.updateStockByOuterProductCaseBarcode),
]
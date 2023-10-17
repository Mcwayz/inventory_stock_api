from django.urls import path
from . import views



# URLs / Routes for endpoints

urlpatterns = [
    path('addInventory/', views.addStock),   
    path('addSection/', views.addSection),
    path('addProduct/', views.addProduct),
    path('getSections/', views.getSections),
    path('getProducts/', views.getProducts),
    path('getInventory/', views.getInventory),
    path('getSection/<str:pk>/', views.getSection),
    path('getProduct/<str:pk>/', views.getProduct),
    path('getInventoryProduct/<str:pk>/', views.getInventoryDetails),
    path('dispatchProduct/', views.updateStockByOuterProductCaseBarcode),
    path('getProductId/', views.getProductInfoByBarcode, name='get_product_id_by_barcode'),
]
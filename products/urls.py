from django.urls import path
from .views import(
    ProductListView, ProductDeleteView, ProductCreateView, ProductUpdateView
)

app_name ='products'
urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('create_product/',ProductCreateView.as_view(), name='create_product' ),  
    path('delete_product<int:pk>/',ProductDeleteView.as_view(), name='delete_product' ),  
    path('update_product<int:pk>/',ProductUpdateView.as_view(), name='update_product' ),  
]
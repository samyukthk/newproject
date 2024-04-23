from django.urls import path
from djangoapp.views import *

urlpatterns = [
    path('Product', Product_list, name='product'),
    path('Productadd/', Product_add, name='product'),
    path('product/<int:product_id>/delete/', Product_delete, name='product-delete'),
    
    
    path('categorylist/',Category_list,name='category'),
    path('category/<int:category_id>/view/', category_view, name='category-view'),
    path('category/<int:category_id>/delete/', category_delete, name='category-delete'),
    path('categoryedit/<int:category_id>/edit2/', category_edit2, name='category-delete'),
    

    
    path('image/list', image_list, name='image-list'), 
    
    path('category/<int:category_id>/products/',  CategoryWithProduct.as_view(), name='category-with-product'),
    path('category/<int:category_id>/productvar/',CategoryWithProductvar.as_view(),name='category-with-product'),
]
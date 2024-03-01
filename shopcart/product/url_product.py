
#url mapper 

from . import views
from django.urls import path

urlpatterns = [
    # path('callme/', views.say_hello),
    path('home/', views.startpage),
    path('',views.startpage),
    path ('addproduct/', views.add_product),
    path ('showprod/', views.showprod),
    path ('editorder/<int:pid>/', views.editproduct, name='edit-order'),
    path ('deleteorder/<int:pid>/', views.deleteproduct, name='delete-order'),
    path ('prod_cat/', views.prod_cat, name='product-catagory'),
    path ('showprodcat/', views.showprodcat, name='show-product-catagory'),
    path ('editprodcat/<int:pcatid>/', views.edit_prodcat, name='edit-prodcat'),
    path ('deleteprodcat/<int:pcatid>/', views.delete_prodcat, name='delete-prodcat'),
    path ('showitemsbycat/<int:cat_id>/', views.prod_list_bycat, name='showitemsbycat'),
    path ('editprodlistbycat/<int:cat_id>/', views.edit_prod_list_bycat, name='editprodlistbycat'),
    path ('deleteprodlistbycat/<int:cat_id>/', views.delete_prod_list_bycat, name='deleteprodlistbycat'),
    path ('search/', views.search_product, name='search'),
    path ('productdetails/<int:product_id>/', views.productdetails, name='productdetails'),
    path ('pagenotfound/',views.not_found_page, name='pagenotfound'),
]

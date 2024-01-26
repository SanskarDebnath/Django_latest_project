#url mapper 



from django.urls import path
from . import views

urlpatterns = [
    path('callme/', views.say_hello),
    path('home/', views.startpage),
    path('',views.startpage),
    path('garments/', views.garmentpage),
    path('mobile/', views.mobilepage),
    path ('test/', views.testpage),
    path ('addproduct/', views.add_product),
    path ('showprod/', views.viewall),
    path ('editorder/<int:pid>/', views.editorder, name='edit-order'),
    path ('deleteorder/<int:pid>/', views.deleteorder, name='delete-order'),
    path ('prod_cat/', views.prod_cat, name='product-catagory')
]

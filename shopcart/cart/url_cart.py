
#url mapper 

from . import views
from django.urls import path

urlpatterns = [
    # path('callme/', views.say_hello),
    path('add/', views.add_cart, name='addcart'),
    # path('',views.startpage),
    path ('cartpage/',views.cart_page, name='cartpage')
]

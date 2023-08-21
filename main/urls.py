from django.urls import path
from .views import test, index, SubcatsApiView, SubcatApiView, CatApiView, PodcatApiView, AddCartItemView, AddCustomerView, view_cart

urlpatterns = [
    path('', test),
    path('api/cats', CatApiView.as_view()),
    path('api/subcatlist', SubcatsApiView.as_view()),
    path('api/subcats/<int:idiot>', PodcatApiView.as_view()),
    path('api/subcat/<int:idiot>', SubcatApiView.as_view()),
    path('cat/<int:id>', index),
    path('api/add-cart-item/', AddCartItemView.as_view(), name='add-cart-item'),
    path('api/add-customer/', AddCustomerView.as_view(), name='add-customer'),
    path('api/viewcart/', view_cart)

]
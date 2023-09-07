from django.urls import path
from .views import test, SubcatsApiView, SubcatApiView, CatApiView, PodcatApiView, AddCartItemView, AddCustomerView, view_cart, GetCustomerId

urlpatterns = [
    path('', test),
    path('api/cats', CatApiView.as_view()),
    path('api/subcatlist', SubcatsApiView.as_view()),
    path('api/subcats/<int:idiot>', PodcatApiView.as_view()),
    path('api/subcat/<int:idiot>', SubcatApiView.as_view()),
    path('api/add-cart-item/', AddCartItemView.as_view(), name='add-cart-item'),
    path('api/add-customer/', AddCustomerView.as_view(), name='add-customer'),
    path('api/viewcart/', view_cart),
    path('api/getid/<int:id>', GetCustomerId)
]
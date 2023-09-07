import json
from django.forms import JSONField
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.serializers import serialize
from .models import Product, SubSubCategory, SubCategory, Category, CartItem, Customer
from django.views.generic import DetailView
from rest_framework import generics
from .serializers import SubcatSerializer, SubcatsSerializer, CatsSerializer, CartItemSerializer, CustomerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from telegram import Bot


def test(request, id):
    products = Product.objects.order_by('-price')
    return render(request, 'main/test.html', {'products': products, 'id': id})


def index(request, id):
    subsubcat_to_filter_prods = SubSubCategory.objects.get(id=id)
    products_to_show = Product.objects.filter(
        father=subsubcat_to_filter_prods.id)
    other_subsubcats_to_be_shown = SubSubCategory.objects.filter(
        father=subsubcat_to_filter_prods.father)
    return render(request, 'main/index.html', {'products': products_to_show, 'subsubcats': other_subsubcats_to_be_shown})


class SubcatsApiView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubcatsSerializer


class SubcatApiView(generics.ListAPIView):
    def get(request, self, *args, **kwargs):
        id = kwargs["idiot"]
        pl = SubSubCategory.objects.filter(father=id).values()
        pl = list(pl)
        for i in list(pl):
            children = list(Product.objects.filter(father=i['id']).values())
            i['children'] = children
        return Response({"products": list(pl)})


class CatApiView(generics.ListAPIView):
    def get(request, self, *args, **kwargs):
        pl = Category.objects.all()
        serialized_data = serialize("json", pl)
        serialized_data = json.loads(serialized_data)
        return Response({'products': serialized_data})


class PodcatApiView(generics.ListAPIView):
    def get(request, self, *args, **kwargs):
        id = kwargs["idiot"]
        pl = SubCategory.objects.filter(father=id).values()
        pl = list(pl)
        return Response({"products": list(pl)})


def view_cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=1)
    context = {'cart_items': cart_items}
    return Response({"via": context})


class AddCartItemView(APIView):
    def post(self, request, format=None):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            bot_token = '6575902703:AAFrxGMsn_tvktZNOmEgd8pg5op5oBAkn9A '
            chat_id = '6173791626'
            bot = Bot(token=bot_token)
            message = "Новый товар в корзине у"
            bot.send_message(chat_id=chat_id, text=message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddCustomerView(APIView):
    def post(self, request, format=None):   
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)




def GetCustomerId(request, *args, **kwargs):
    user_tgid = kwargs["id"]
    user_id = Customer.objects.filter(telegram_id=user_tgid ).values()
    return JsonResponse({"id": list(user_id[0]["id"])})


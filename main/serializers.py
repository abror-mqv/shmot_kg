from rest_framework import serializers
from .models import SubCategory, Product, Category, CartItem, Customer

class SubcatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ('subcat_name', 'father')

class SubcatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_name', 'father')

class CatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('cat_name')

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('name', "number")


from .models import Category, Product, ProductVariant, ImageTest
from rest_framework  import serializers




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model =Product
        
        fields = '__all__'
 
 
 
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
 
 
 
        
class ProductVariantSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductVariant
        fields = '__all__'
        
        
class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageTest
        fields = '__all__'
        
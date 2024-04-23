from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from djangoapp.models import *
from djangoapp.serializers import *
from djangoapp.models import *
from rest_framework.decorators import api_view, APIView
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def Product_list(request):
    if request.method == 'GET':
        account = Product.objects.all()
        serializers = ProductSerializer(account, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def Product_add(request):
    if request.method == 'GET':
        account = Product.objects.all()
        serializers = ProductSerializer(account, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'DELETE'])
def Product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method ==  'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def _str_(self):
        return self.name 
    
    
    
@api_view(['GET'])
def Category_list(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    
    
@api_view(['GET'])
def category_view(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method ==  'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET', 'DELETE'])
def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method ==  'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
@api_view(['GET', 'PUT'])
def category_edit2(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
       
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

@api_view(['GET'])
def image_list(request):
    if request.method == 'GET':
        image = ImageTest.objects.all()
        serializer = ImageSerializer(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
########################################### with class #########################################   


class CategoryWithProduct(APIView):
    def get(self, request, category_id, format=None):
        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=status.HTTP_404_NOT_FOUND)

        category_serializer = CategorySerializer(category)
        products = Product.objects.filter(category=category)
        products_serializer = ProductSerializer(products, many=True)

        

        response_data = {
            'category': category_serializer.data,
            'products': products_serializer.data,
        }

        return Response(response_data, status=status.HTTP_200_OK)



    
class CategoryWithProductvar(APIView):
    def get(self, request, category_id, format=None):
        try: 
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            return Response({'error':'Category not found'}, status=status.HTTP_404_NOT_FOUND) 
        category_serializer = CategorySerializer(category)
        products = Product.objects.filter(category=category)

        product_data = []
        for product in products:
            product_serializer = ProductSerializer(product)
            products_var = ProductVariant.objects.filter(product=product)
            productvar_serializer = ProductVariantSerializer(products_var, many=True)
            product_data.append({
                'product': product_serializer.data,
                'variants': productvar_serializer.data
            })        

        response_maindata = {
            'category': category_serializer.data,
            'All products & its variants of the selected category': product_data
        }

        return Response(response_maindata, status=status.HTTP_200_OK)


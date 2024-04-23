from django.shortcuts import render
from rest_framework.decorators import api_view ,APIView
from rest_framework.response import Response
from studentapp.serializers import  *
from rest_framework import status
from studentapp.serializers import *
from studentapp.models import *
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST'])
def student_add(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializers = StudentSerializer(student, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET'])
def student_list(request):
    if request.method == 'GET':
        student = Student.objects.all()
        serializers = StudentSerializer(student, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    


@api_view(['GET', 'DELETE'])
def student_delete(request, student_id):
    student = Student.objects.get(id=student_id)
    if request.method ==  'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
 
 
 ############################################school############################################################   
  
  
    
@api_view(['GET','POST'])
def school_add(request):
    if request.method == 'GET':
        school = School.objects.all()
        serializers = SchoolSerializer(school, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializers = SchoolSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET'])
def school_list(request):
    if request.method == 'GET':
        school = School.objects.all()
        serializers = SchoolSerializer(school, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    
    
    
@api_view(['GET', 'DELETE'])
def school_delete(request, school_id):
    school = School.objects.get(id=school_id)
    if request.method ==  'GET':
        serializer = SchoolSerializer(school)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        school.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
###################################### batch ##############################################################




@api_view(['GET','POST'])
def batch_add(request):
    if request.method == 'GET':
        batch = Batch.objects.all()
        serializers = SchoolSerializer(batch, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    elif request.method=='POST':
        serializers = BatchSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET'])
def batch_list(request):
    if request.method == 'GET':
        batch = Batch.objects.all()
        serializers = BatchSerializer(batch, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)
    
    
    
    
@api_view(['GET', 'DELETE'])
def batch_delete(request, batch_id):
    batch = Batch.objects.get(id=batch_id)
    if request.method ==  'GET':
        serializer = SchoolSerializer(batch)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        batch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
    
######################################  function  #########################################



class SchoolList(APIView):
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
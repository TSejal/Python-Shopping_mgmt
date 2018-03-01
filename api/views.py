from django.shortcuts import render
from Shopping_models.models import *
from Shopping_models.serializers import *
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q

# Create your views here.

# Users
# 16
@api_view(['GET'])
def all_users(request):
    result = User.objects.filter(Q(is_active = 'True') & Q(country = 'India'))
    serializer = UserSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)

@api_view(['GET'])
def list_users(request):
    result = User.objects.all()
    serializer = UserSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)

@api_view(['POST'])
def add_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
# 17

@api_view(['POST'])
def add_seller(request):
    serializer = SellerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def sellers_enabled(request):
    result = Seller.objects.filter(Q(enabled = 'True') & Q(profile__country = 'USA'))
    serializer = SellerSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)

# 18

@api_view(['POST'])
def add_product(request):
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['GET'])
def products_outOfStock(request):
    result = Product.objects.filter(quantity = 0)
    serializer = ProductSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)

# 19
@api_view(['GET'])
def products(request):
    sellers = Seller.objects.filter(enabled=True)
    result = Product.objects.filter(added_by__in = sellers)
    serializer = ProductSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)

# 20
@api_view(['GET'])
def top5_products(request):
    result = Product.objects.all().order_by('-unit_sold')[:5]
    serializer = ProductSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)

# 21
@api_view(['GET'])
def unpublish_outofStock_products(request):
    result = Product.objects.filter(quantity = 0)
    for i in result:
        i.publish_status = False
        i.save()
    serializer = ProductSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)

# 22
@api_view(['GET'])
def products2(request):
    result = Product.objects.filter(Q(title__startswith = 'Sam') & Q(price__gt = 100))
    serializer = ProductSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)

# 23
@api_view(['GET'])
def products3(request):
    result = Product.objects.exclude(title = 'ple')
    count = result.count()
    return Response({'Number of records which title is not contains "ple"... ':count}, status=status.HTTP_200_OK)

# 24
@api_view(['GET'])
def products4(request):
    result = Product.objects.filter(Q(category = 'Mobiles') | Q(category = 'Shoes') & Q(price__gt = 100) & Q(price__lt = 5000))
    serializer = ProductSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)



# 25
@api_view(['GET'])
def products5(request):
    result = Product.objects.filter(publish_status = 'True').order_by('-date_added')[:5]
    serializer = ProductSerializer(result, many = True)
    return Response(serializer.data, status=status.HTTP_302_FOUND)
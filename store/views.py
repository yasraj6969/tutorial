from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializers

# Create your views here.

@api_view()
def product_list(request):
    queryset = Product.objects.all()
    serializer = ProductSerializers(queryset,many=True)
    return Response(serializer.data)

@api_view()
def product_detail(request,id):
    # try:
    # product = Product.objects.get(pk=id)
    product = get_object_or_404(Product,pk=id)
    serializer = ProductSerializers(product)
    return Response(serializer.data)
    # except Product.DoesNotExist:
        # return Response(status=status.HTTP_404_NOT_FOUND)
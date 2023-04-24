from django.shortcuts import render
from . serializers import CartSerializerPost, CartSerializerGet
from . models import Cart
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework import status

# Create your views here.


class CartView(APIView):
    serializer_class = CartSerializerPost
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None, *args, **kwargs):
        if id:
            try:
                data = Cart.objects.get(id=id)
                serializer = CartSerializerGet(data)
                return Response(serializer.data)
            except Cart.DoesNotExist:
                return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            data = Cart.objects.all()
            serializer = CartSerializerGet(data, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CartSerializerPost(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully saved", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, *args, **kwargs):
        try:
            CategoryData = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = CartSerializerPost(
            instance=CategoryData, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully Updated", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_200_OK)

    def delete(self, request, id, *args, **kwargs):
        try:
            CartData = Cart.objects.get(id=id)
        except Cart.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        CartData.delete()
        return Response({"Response": "Data is Successfully Deleted"}, status=status.HTTP_200_OK)

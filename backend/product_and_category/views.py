from rest_framework.response import Response
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework import status


class ProductView(APIView):
    serializer_class = ProductSerializer
    # permission_classes=[IsAuthenticated]

    def get(self, request, id=None, *args, **kwargs):
        if id:
            try:
                data = Product.objects.get(id=id)
                serializer = ProductSerializer(data)
                return Response(serializer.data)
            except Product.DoesNotExist:
                return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            data = Product.objects.all()
            serializer = ProductSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully saved", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, *args, **kwargs):
        try:
            ProductData = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = ProductSerializer(instance=ProductData, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully Updated", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        try:
            ProductData = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        ProductData.delete()
        return Response({"Response": "Data is Successfully Deleted"}, status=status.HTTP_200_OK)


class CategoryView(APIView):
    serializer_class = CategorySerializer
    # permission_classes=[IsAuthenticated]

    def get(self, request, id=None, *args, **kwargs):
        if id:
            try:
                data = Category.objects.get(id=id)
                serializer = CategorySerializer(data)
                return Response(serializer.data)
            except Category.DoesNotExist:
                return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            data = Category.objects.all()
            serializer = CategorySerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully saved", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, *args, **kwargs):
        try:
            CheckoutData = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = CategorySerializer(
            instance=CheckoutData, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully Updated", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        try:
            CheckoutData = Category.objects.get(id=id)
        except Category.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        CheckoutData.delete()
        return Response({"Response": "Data is Successfully Deleted"}, status=status.HTTP_200_OK)

from django.shortcuts import render
from . serializers import CheckoutSerializerPost, CheckoutSerializerGet
from . models import Checkout
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CheckoutView(APIView):
    serializer_class = CheckoutSerializerPost
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None, *args, **kwargs):
        if id:
            try:
                data = Checkout.objects.get(id=id)
                serializer = CheckoutSerializerGet(data)
                return Response(serializer.data)
            except Checkout.DoesNotExist:
                return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            data = Checkout.objects.all()
            serializer = CheckoutSerializerGet(data, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CheckoutSerializerPost(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully saved", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, *args, **kwargs):
        try:
            CheckoutData = Checkout.objects.get(id=id)
        except Checkout.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = CheckoutSerializerPost(
            instance=CheckoutData, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully Updated", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        try:
            CheckoutData = Checkout.objects.get(id=id)
        except Checkout.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        CheckoutData.delete()
        return Response({"Response": "Data is Successfully Deleted"}, status=status.HTTP_200_OK)

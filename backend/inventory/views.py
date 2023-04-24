from rest_framework.response import Response
from .serializers import InventorySerializer
from .models import Inventory
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Create your views here.


class InventoryView (APIView):
    serializer_class = InventorySerializer
    # permission_classes = [IsAuthenticated]

    def get(self, request, id=None, *args, **kwargs):
        if id:
            try:
                data = Inventory.objects.get(id=id)
                serializer = InventorySerializer(data)
                return Response(serializer.data)
            except Inventory.DoesNotExist:
                return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            data = Inventory.objects.all()
            serializer = InventorySerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = InventorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully saved", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, *args, **kwargs):
        data = request.data
        try:
            ProductData = Inventory.objects.get(id=id)
        except Inventory.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = InventorySerializer(instance=ProductData, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully Updated", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        try:
            ProductData = Inventory.objects.get(id=id)
        except Inventory.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        ProductData.delete()
        return Response({"Response": "Data is Successfully Deleted"}, status=status.HTTP_200_OK)

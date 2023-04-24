from rest_framework.response import Response
from .serializers import OrderSerializer
from .models import Order
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


class OrderView(APIView):
    serializer_class = OrderSerializer
    # permission_classes=[IsAuthenticated]

    def get(self, request, id=None, *args, **kwargs):
        if id:
            try:
                data = Order.objects.get(id=id)
                serializer = OrderSerializer(data)
                return Response(serializer.data)
            except Order.DoesNotExist:
                return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            data = Order.objects.all()
            serializer = OrderSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = OrderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully saved", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id, *args, **kwargs):
        try:
            OrderData = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data
        serializer = OrderSerializer(instance=OrderData, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Response": "Data is Successfully Updated", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, *args, **kwargs):
        try:
            OrderData = Order.objects.get(id=id)
        except Order.DoesNotExist:
            return Response({"Response": "Data not found"}, status=status.HTTP_404_NOT_FOUND)
        OrderData.delete()
        return Response({"Response": "Data is Successfully Deleted"}, status=status.HTTP_200_OK)

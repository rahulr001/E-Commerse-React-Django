from rest_framework import serializers
from . models import Checkout
from cart.serializers import CartSerializerGet

class CheckoutSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = Checkout
        fields = ['Cart','CustomerName','MobileNumber','DeliveryAddress','PaymentMode']

    
    def create(self, validated_data):
        # Get the cart items from the validated data
        cart_items = validated_data.pop('Cart')

        # Create the checkout instance
        checkout = Checkout.objects.create(**validated_data)

        # Loop through the cart items and reduce the ProductStock
        for cart_item in cart_items:
            product = cart_item.Product
            quantity = cart_item.Quantity

            # Reduce the ProductStock field
            product.ProductStock -= quantity
            product.save()

            # Add the cart item to the checkout
            checkout.Cart.add(cart_item)

        return checkout

class CheckoutSerializerGet(serializers.ModelSerializer):
    Cart = CartSerializerGet(many = True)

    class Meta:
        model = Checkout
        fields = "__all__"

from rest_framework import serializers
from .models import Product, OrderItem, Order
from django.contrib.auth.models import User

class ResigistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Override the create method to create a user with a hashed password (User.objects.user -> User.objects.create_user)
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'total_price', 'created_at', 'items']    
        read_only_fields = ['user', 'total_price', 'created_at'] 

class OrderCreateSerializer(serializers.Serializer):
    products = serializers.ListField(
        child=serializers.IntegerField()
    )

    def create(self, validated_data):
        user = self.context['request'].user
        products = validated_data.pop('products')
        order = Order.objects.create(user=user)
        total_price = 0
        for product in products:
            product_id = product.get("product_id")
            quantity = product.get("quantity")
            product = Product.objects.get(id=product_id)
            price = product.price * quantity

            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)
            total_price += price

        order.total_price = total_price
        order.save()
        return super().create(validated_data)
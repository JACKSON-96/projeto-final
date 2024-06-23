# order/viewsets.py

from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order  # Certifique-se de que o modelo Order está no arquivo models.py

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

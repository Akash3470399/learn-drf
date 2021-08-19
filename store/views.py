from rest_framework import viewsets

from .serializers import StoreSerializer
from .models import Store

class StoreViewset(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
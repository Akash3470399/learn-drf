from rest_framework.generics import ListCreateAPIView,\
 RetrieveUpdateDestroyAPIView

from .serializers import StoreSerializer
from .models import Store

class StoreList(ListCreateAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

class StoreView(RetrieveUpdateDestroyAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    
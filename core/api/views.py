from .serializers import ItemSerializer
from core.models import Item
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny


class ItemListAPIView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

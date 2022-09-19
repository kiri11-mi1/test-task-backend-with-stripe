from rest_framework import viewsets, mixins

from ...items.models import Item
from ..serializers import BuyRetrieveSerializer


class BuyViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Item.objects.all()

    serializer_class = BuyRetrieveSerializer

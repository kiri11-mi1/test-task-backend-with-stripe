from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from ...items.models import Item
from ..serializers import BuyRetrieveSerializer
from ..service import StripeAPI


class BuyViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = Item.objects.all()

    serializer_class = BuyRetrieveSerializer

    def retrieve(self, request, *args, **kwargs):
        item = self.get_object()
        stripe_api = StripeAPI(item.price)
        serializer = self.serializer_class(data=stripe_api.create_session())
        serializer.is_valid()

        return Response(serializer.data, status=status.HTTP_200_OK)

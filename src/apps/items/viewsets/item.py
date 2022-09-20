import os

from rest_framework import viewsets, mixins
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from ...items.models import Item


class ItemViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    renderer_classes = [TemplateHTMLRenderer]
    queryset = Item.objects.all()
    template_name = 'detail.html'

    def retrieve(self, request, *args, **kwargs):
        return Response(
            {
                'item': self.get_object(),
                'stripe_publish_key': os.environ.get('STRIPE_API_PUBLISH_KEY')
            },
            template_name='items_detail.html'
        )

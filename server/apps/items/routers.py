from rest_framework.routers import DefaultRouter

from .viewsets import ItemViewSet, BuyViewSet

items_router = DefaultRouter()

items_router.register(
    prefix='item',
    viewset=ItemViewSet,
    basename='item',
)

items_router.register(
    prefix='buy',
    viewset=BuyViewSet,
    basename='buy',
)

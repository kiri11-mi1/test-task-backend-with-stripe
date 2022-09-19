from rest_framework.routers import DefaultRouter

from .viewsets import BuyViewSet

buy_router = DefaultRouter()

buy_router.register(
    prefix='buy',
    viewset=BuyViewSet,
    basename='buy',
)

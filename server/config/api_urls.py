from django.urls import path, include

from apps.buy.routers import buy_router


urlpatterns = [
    path('buy/', include(buy_router.urls)),
]

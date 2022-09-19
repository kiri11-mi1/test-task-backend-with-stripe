from django.urls import path, include

from apps.items.routers import items_router


urlpatterns = [
    path('items/', include(items_router.urls)),
]

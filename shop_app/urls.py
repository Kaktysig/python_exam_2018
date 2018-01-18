from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from shop_app.views import ProfileView, ShopView, CartView


router = DefaultRouter()
router.register(r'profile', ProfileView)
router.register(r'shop', ShopView)
router.register(r'cart', CartView)


urlpatterns = [
    # Endpoints:
    url(r'', include(router.urls))
]

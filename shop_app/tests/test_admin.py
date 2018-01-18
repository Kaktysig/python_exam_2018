import pytest
from django.contrib.admin.sites import AdminSite

from shop_app.admin import Admin_Goods_Variation, Admin_Cart
from shop_app.models import Goods_Variation, Good, Category, Cart, Customer


@pytest.mark.django_db
def test_admin_goods_variation():
    site = AdminSite()
    category = Category(name="Test")
    category.save()
    good = Good(name="TestGood", category=category)
    good.save()
    good_var = Goods_Variation(variation_name="TestGoodVar", parent=good, description="TestDesc", cost=100)
    good_var.save()
    admin_class = Admin_Goods_Variation(Goods_Variation, site)
    assert admin_class.get_parent_name(good_var) == "TestGood"


@pytest.mark.django_db
def test_admin_cart():
    site = AdminSite()
    user = Customer(username="TestUser", email="user@test.ru")
    user.save()
    category = Category(name="Test")
    category.save()
    good = Good(name="TestGood", category=category)
    good.save()
    good_var = Goods_Variation(variation_name="TestGoodVar", parent=good, description="TestDesc", cost=100)
    good_var.save()
    cart = Cart(customer=user)
    cart.save()
    admin_class = Admin_Cart(Cart, site)
    assert admin_class.good_count(cart) == 0
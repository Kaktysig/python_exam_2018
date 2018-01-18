import pytest
from django.shortcuts import get_object_or_404


@pytest.mark.django_db
def test_customer():
    from shop_app.models import Customer

    user = Customer(username="TestUser", email="user@test.ru")
    user.save()
    test_user = get_object_or_404(Customer, email=user.email)

    assert str(test_user) == user.username


@pytest.mark.django_db
def test_category():
    from shop_app.models import Category

    category = Category(name="Test")
    category.save()
    test_category = get_object_or_404(Category, name=category.name)

    assert str(test_category) == category.name


@pytest.mark.django_db
def test_good():
    from shop_app.models import Category, Good

    category = Category(name="Test")
    category.save()

    good = Good(name="TestGood", category=category)
    good.save()
    test_good = get_object_or_404(Good, name=good.name)

    assert str(test_good) == good.name
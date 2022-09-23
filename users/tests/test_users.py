import pytest

from users.models import CustomUser


@pytest.fixture
def user_collector(db):
    email = 'test123@email.com'
    username = 'Fred123'
    first_name = 'Fred'
    last_name = 'Robson'
    is_collector = True
    is_active = True
    is_staff = True
    return CustomUser.objects.create(email=email, username=username, first_name=first_name,
                                     last_name=last_name, is_collector=is_collector,
                                     is_active=is_active, is_staff=is_staff)


@pytest.fixture
def user_sales_manager(db):
    email = 'sales123@email.com'
    username = 'Bobby321'
    first_name = 'Bobby'
    last_name = 'Bob'
    is_sales_manager = True
    is_active = True
    is_staff = True
    return CustomUser.objects.create(email=email, username=username, first_name=first_name,
                                     last_name=last_name, is_sales_manager=is_sales_manager,
                                     is_active=is_active, is_staff=is_staff)


def test_user_login_fail(client):
    response = client.get('/')
    assert response.status_code == 200


def test_user_login(client, django_user_model):
    email = "test_sales_manager@email.com"
    password = "TestPass123"
    first_name = 'Test'
    last_name = 'Test'
    user = django_user_model.objects.create_user(email=email, password=password,
                                                 first_name=first_name, last_name=last_name)
    client.force_login(user)
    response = client.get('/')
    assert response.status_code == 200


def test_collector(user_collector):
    assert CustomUser.objects.filter(email=user_collector.email).exists()


def test_sales_manager(user_sales_manager):
    assert CustomUser.objects.filter(email=user_sales_manager.email).exists()

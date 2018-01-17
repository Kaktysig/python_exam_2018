import pytest


@pytest.mark.django_db
def test_status_code(client):
    response = client.get('/')
    assert response.status_code == 200

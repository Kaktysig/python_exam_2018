# -*- coding: utf-8 -*-

import pytest


@pytest.mark.acceptance
@pytest.mark.django_db
def test_create_new_profile(client):
    response = client.post('/api/v1/profile/', {
    "email": "some@mail.ru",
    "username": "useruser",
    "password": "qweqwe",
})
    assert response.status_code == 201


# @pytest.mark.acceptance
# def test_login(client):
#     """
#     This test should login into the existing account.
#     This test should assert that jwt token is returned in the response.
#     Also, this test should assert the response code.
#     Which should equal to `200`.
#     """
#     raise NotImplemented('Acceptance test failed')
#
#
# @pytest.mark.acceptance
# def test_login_bad_credentials(client):
#     """
#     This test should not login into the existing account.
#     This test should assert that it is
#     impossible to login with bad email/password pair.
#     Also, this test should assert the response code.
#     Which should equal to `401`.
#     """
#     raise NotImplemented('Acceptance test failed')
#
#
# @pytest.mark.acceptance
# def test_current_profile(client):
#     """
#     This test should get the information about the current user.
#     This test should assert that response has correct values.
#     Also, this test should assert the response code.
#     Which should equal to `200`.
#     """
#     raise NotImplemented('Acceptance test failed')
#
#
# @pytest.mark.acceptance
# def test_current_profile_history(client):
#     """
#     This test should get the order history for the current user.
#     This test should assert that response has correct values.
#     Also, this test should assert the response code.
#     Which should equal to `200`.
#     """
#     raise NotImplemented('Acceptance test failed')
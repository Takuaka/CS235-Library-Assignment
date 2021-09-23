import pytest

from flask import session


def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Lockdown Library' in response.data


def test_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert b'Book Title' in response.data
    assert b'Book ID' in response.data

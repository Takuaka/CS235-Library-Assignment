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


def test_book_details(client):
    response = client.get('/book_details/4432')
    assert response.status_code == 200
    assert b'The Secret Hour' in response.data
    assert b'Publisher: HarperCollins' in response.data
    assert b'Book ID: 4432' in response.data
    assert b'Not available as eBook' in response.data
    assert b'Page number: 297' in response.data

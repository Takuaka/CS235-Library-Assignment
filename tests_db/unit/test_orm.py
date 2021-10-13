import pytest

from sqlalchemy.exc import IntegrityError

from library.domain.model import Publisher, Author, Book

def insert_book(empty_session):
    pass
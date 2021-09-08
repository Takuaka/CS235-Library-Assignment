import pytest

from library.domain.model import Publisher, Author, Book
from library.adapters.repository import RepositoryException


def test_repository_can_get_book(in_memory_repo):
    book = in_memory_repo.get_book(1)

    pass


def test_repository_can_get_first_book(in_memory_repo):
    book = in_memory_repo.get_first_book()

    pass


def test_repository_can_get_last_book(in_memory_repo):
    book = in_memory_repo.get_last_book()

    pass


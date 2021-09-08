import pytest

from library.domain.model import Publisher, Author, Book
from library.adapters.repository import RepositoryException


def test_repository_can_get_book(in_memory_repo):
    book = in_memory_repo.get_book(2)
    assert book.book_id == 5251
    assert book.title == "Skulduggery Pleasant"


def test_repository_can_get_first_book(in_memory_repo):
    book = in_memory_repo.get_first_book()
    assert book.book_id == 4432
    assert book.title == "The Secret Hour"


def test_repository_can_get_last_book(in_memory_repo):
    book = in_memory_repo.get_last_book()
    assert book.book_id == 6431
    assert book.title == "StormFront"


def test_repository_can_add_book(in_memory_repo):
    book = Book(9999, "The Mist")
    in_memory_repo.add_book(book)
    assert in_memory_repo.get_book(5) is book


def test_repository_does_not_get_book_that_does_not_exist(in_memory_repo):
    book = in_memory_repo.get_book(7)
    assert book is None


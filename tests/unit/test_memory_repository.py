import pytest

from library.domain.model import Publisher, Author, Book
from library.adapters.repository import RepositoryException


def test_repository_returns_list_of_books(in_memory_repo):
    test_list = in_memory_repo.books_list
    assert test_list[0].book_id == 0


def test_repository_can_get_book(in_memory_repo):
    book = in_memory_repo.get_book(5251)
    assert book.book_id == 5251
    assert book.title == "Skulduggery Pleasant"


def test_repository_can_get_first_book_id(in_memory_repo):
    book_id = in_memory_repo.get_first_book_id()
    assert book_id == 0


def test_repository_can_get_last_book_id(in_memory_repo):
    book_id = in_memory_repo.get_last_book_id()
    assert book_id == 6431


def test_repository_can_add_book(in_memory_repo):
    book = Book(9999, "The Mist")
    in_memory_repo.add_book(book)
    assert in_memory_repo.get_book(9999) is book


def test_repository_does_not_get_book_that_does_not_exist(in_memory_repo):
    book = in_memory_repo.get_book(4656)
    assert book is None


def test_repository_returns_prev_and_next_ids(in_memory_repo):
    prev_id, next_id = in_memory_repo.get_prev_next_books_ids(1153)
    assert prev_id == 666
    assert next_id == 4432


def test_repository_returns_none_when_required_prev_next_ids(in_memory_repo):
    prev_none_id, next_id = in_memory_repo.get_prev_next_books_ids(0)
    prev_id, next_none_id = in_memory_repo.get_prev_next_books_ids(6431)

    assert prev_none_id is None
    assert next_none_id is None
    assert prev_id == 5251
    assert next_id == 666

# author stuff


def test_repository_can_get_author(in_memory_repo):
    author = in_memory_repo.get_author(1425)
    assert author.full_name == "Scott Westerfield"


def test_repository_correctly_adds_coauthors(in_memory_repo):
    author1 = in_memory_repo.get_author(6676)
    author2 = in_memory_repo.get_author(4200)
    assert author1.check_if_this_author_coauthored_with(author2)
    assert author2.check_if_this_author_coauthored_with(author1)
    assert author1.check_if_this_author_coauthored_with(author1) is False

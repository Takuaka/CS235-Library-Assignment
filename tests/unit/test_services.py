import pytest

from library.books.services import NonExistentBookException
from library.books import services as book_services

from library.authors.services import NonExistentAuthorException
from library.authors import services as author_services


def test_get_book(in_memory_repo):
    book = book_services.get_book(1153, in_memory_repo)
    assert book['title'] == "The Amulet of Samarkand"
    assert book['authors'] == ['Jonathan Stroud']
    assert book['publisher'] == "Doubleday"
    assert book['page_num'] == 462
    assert book['book_id'] == 1153
    assert book['is_ebook'] is True


def test_cannot_get_book_with_non_existent_id(in_memory_repo):
    book_id = 99586
    with pytest.raises(book_services.NonExistentBookException):
        book_services.get_book(book_id, in_memory_repo)


def test_book_to_dict_conditionals(in_memory_repo):
    book = book_services.get_book(0, in_memory_repo)
    assert book['publisher'] == "Not available"
    assert book['page_num'] == "Not available"


def test_get_prev_next_book_ids(in_memory_repo):
    prev_id, next_id = book_services.get_prev_next_books_ids(1153, in_memory_repo)
    assert prev_id == 666
    assert next_id == 4432


def test_get_prev_next_book_ids_return_none_when_required(in_memory_repo):
    prev_zero_id, next_id = book_services.get_prev_next_books_ids(0, in_memory_repo)
    assert next_id == 666
    assert prev_zero_id is None

    prev_id, next_zero_id = book_services.get_prev_next_books_ids(6431, in_memory_repo)
    assert prev_id == 5251
    assert next_zero_id is None


def test_get_book_dict(in_memory_repo):
    test_dict = book_services.get_book_dict(in_memory_repo)
    assert test_dict[6431] == "Storm Front"

# Author tests


def test_get_author(in_memory_repo):
    author1 = author_services.get_author(6676, in_memory_repo)
    assert author1['author_full_name'] == 'Neil Gaiman'
    assert author1['author_id'] == 6676
    assert author1['books'] == [666]
    assert author1['coauthors'] == [4200]
    author2 = author_services.get_author(1425, in_memory_repo)
    assert author2['coauthors'] == []


def test_cannot_get_author_with_nonexistent_id(in_memory_repo):
    test_id = 1
    with pytest.raises(author_services.NonExistentAuthorException):
        author_services.get_author(1, in_memory_repo)


def test_get_author_dict(in_memory_repo):
    test_dict = author_services.get_author_dict(in_memory_repo)
    assert test_dict[5525] == "Jim Butcher"

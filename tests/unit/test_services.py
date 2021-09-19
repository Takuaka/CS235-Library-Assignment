import pytest

from library.books.services import NonExistentBookException
from library.books import services as services


def test_get_keys_list(in_memory_repo):
    keys_list = services.get_keys_list(in_memory_repo)
    assert 4432 in keys_list


def test_get_book(in_memory_repo):
    book = services.get_book(1153, in_memory_repo)
    assert book['title'] == "The Amulet of Samarkand"
    assert book['authors'] == ['Jonathan Stroud']
    assert book['publisher'] == "Doubleday"
    assert book['page_num'] == 462
    assert book['book_id'] == 1153
    assert book['is_ebook'] is True


def test_cannot_get_book_with_non_existent_id(in_memory_repo):
    book_id = 99586
    with pytest.raises(services.NonExistentBookException):
        services.get_book(book_id, in_memory_repo)


def test_book_to_dict_conditionals(in_memory_repo):
    book = services.get_book(0, in_memory_repo)
    assert book['publisher'] == "Not available"
    assert book['page_num'] == "Not available"

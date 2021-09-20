from typing import Iterable

from library.domain.model import Publisher, Author, Book
from library.adapters.repository import AbstractRepository


class NonExistentBookException(Exception):
    pass


def get_book_dict(repo: AbstractRepository):
    book_list = repo.books_list
    services_dict = dict()
    for book in book_list:
        services_dict[book.book_id] = book.title
    return services_dict


def get_book(book_id: int, repo: AbstractRepository):
    book = repo.get_book(book_id)
    if book is None:
        raise NonExistentBookException

    return book_to_dict(book)


def get_prev_next_books_ids(book_id: int, repo: AbstractRepository):
    prev_book_id, next_book_id = repo.get_prev_next_books_ids(book_id)
    return prev_book_id, next_book_id


def get_first_last_books_ids(repo: AbstractRepository):
    first_id = repo.get_first_book_id()
    last_id = repo.get_last_book_id()
    return first_id, last_id


###################################

# Book to Dict conversion

###################################


def book_to_dict(book: Book):
    authors = []
    if len(book.authors) > 0:
        for author in book.authors:
            authors.append(author.full_name)

    page_num = "Not available"
    if book.num_pages is not None:
        page_num = book.num_pages

    publisher = "Not available"
    if book.publisher != Publisher(""):
        publisher = book.publisher.name

    book_dict = {
        'book_id': book.book_id,
        'title': book.title,
        'authors': authors,
        'page_num': page_num,
        'publisher': publisher,
        'is_ebook': book.ebook,
        'description': book.description
    }
    return book_dict

def books_to_dict(books: Iterable[Book]):
    return [book_to_dict(book) for book in books]

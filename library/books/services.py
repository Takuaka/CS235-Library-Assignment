from typing import Iterable

from library.domain.model import Publisher, Author, Book
from library.adapters.repository import AbstractRepository


class NonExistentBookException(Exception):
    pass


def get_keys_list(repo: AbstractRepository):
    return repo.get_books_keys_list()


def get_book(book_id: int, repo: AbstractRepository):
    book = repo.get_book(book_id)
    if book is None:
        raise NonExistentBookException

    return book_to_dict(book)


def get_books_dict(repo: AbstractRepository):
    services_books_dict = dict()
    domain_books_dict = repo.get_books_dict()
    for key in domain_books_dict.keys():
        services_books_dict[key] = domain_books_dict[key].title
    return services_books_dict


def book_to_dict(book: Book):

    authors = "Not available"
    if len(book.authors) > 0:
        authors = []
        for author in book.authors:
            authors.append(author.full_name)

    page_num = "Not Available"
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

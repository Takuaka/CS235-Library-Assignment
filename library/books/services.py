from typing import Iterable

from library.domain.model import Publisher, Author, Book
from library.adapters.repository import AbstractRepository


def get_keys_list(repo: AbstractRepository):
    return repo.get_books_keys_list()


def get_books_dict(repo: AbstractRepository):
    return repo.get_books_dict()


def book_to_dict(book: Book):
    book_dict = {
        'book_id': book.book_id,
        'title': book.title,
        'authors': book.authors,
        'page_number': book.num_pages,
        'publisher': book.publisher,
        'is_ebook': book.ebook,
        'description': book.description
    }
    return book_dict


def books_to_dict(books: Iterable[Book]):
    return [book_to_dict(book) for book in books]

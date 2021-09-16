from typing import Iterable

from library.domain.model import Publisher, Author, Book


def book_keys_list(books: Iterable[Book]):
    return [book.book_id for book in books]


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

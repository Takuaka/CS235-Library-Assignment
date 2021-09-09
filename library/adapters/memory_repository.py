import json
from pathlib import Path

from bisect import bisect, bisect_left, insort_left

from library.adapters.jsondatareader import BooksJSONReader
from library.adapters.repository import AbstractRepository, RepositoryException
from library.domain.model import Publisher, Author, Book


class MemoryRepository(AbstractRepository):
    def __init__(self):
        self.__books = list()
        self.__books_index = dict()

    def add_book(self, book: Book):
        insort_left(self.__books, book)
        self.__books_index[book.book_id] = book

    def get_book(self, book_id: int):
        book = None

        try:
            book = self.__books_index[book_id]
        except KeyError:
            pass
        return book

    def get_first_book(self):
        book = None

        if len(self.__books) > 0:
            book = self.__books[0]
        return book

    def get_last_book(self):
        book = None

        if len(self.__books) > 0:
            book = self.__books[-1]
        return book


def load_books(data_path: Path, repo: MemoryRepository):
    books_filename = str(data_path / "comic_books_excerpt.json")
    authors_filename = str(data_path / "book_authors_excerpt.json")
    books = BooksJSONReader(books_filename, authors_filename)
    books.read_json_files()
    for book in books.dataset_of_books:
        repo.add_book(book)


def populate(data_path: Path, repo: MemoryRepository):
    load_books(data_path, repo)


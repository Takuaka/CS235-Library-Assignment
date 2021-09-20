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
        if book not in self.__books:
            insort_left(self.__books, book)
            self.__books_index[book.book_id] = book

    def get_book(self, book_id: int):
        book = None

        try:
            book = self.__books_index[book_id]
        except KeyError:
            pass
        return book

    def get_first_book_id(self):
        first_id = None

        if len(self.__books) > 0:
            first_id = self.__books[0].book_id
        return first_id

    def get_last_book_id(self):
        last_id = None

        if len(self.__books) > 0:
            last_id = self.__books[-1].book_id
        return last_id

    def get_books_keys_list(self):
        return list(self.__books_index.keys())

    def get_books_dict(self):
        return self.__books_index

    # NOT TESTED

    def get_prev_next_books(self, curr_book_id: int):
        id_index = self.__books.index(self.get_book(curr_book_id))
        prev_book_id = None
        next_book_id = None

        if id_index > 0:
            prev_book_id = self.__books[id_index - 1].book_id
        if id_index < (len(self.__books)-1):
            next_book_id = self.__books[id_index + 1].book_id
        return prev_book_id, next_book_id


def load_books(data_path: Path, repo: MemoryRepository):
    books_filename = str(data_path / "comic_books_excerpt.json")
    authors_filename = str(data_path / "book_authors_excerpt.json")
    books = BooksJSONReader(books_filename, authors_filename)
    books.read_json_files()
    for book in books.dataset_of_books:
        repo.add_book(book)


def populate(data_path: Path, repo: MemoryRepository):
    load_books(data_path, repo)

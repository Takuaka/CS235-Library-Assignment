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
        # not tested
        self.__authors = list()
        self.__authors_index = dict()

    def books_list(self):
        return self.__books

    def authors_list(self):
        return self.__authors

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

    def get_prev_next_books_ids(self, curr_book_id: int):
        id_index = self.__books.index(self.get_book(curr_book_id))
        prev_book_id = None
        next_book_id = None

        if id_index > 0:
            prev_book_id = self.__books[id_index - 1].book_id
        if id_index < (len(self.__books)-1):
            next_book_id = self.__books[id_index + 1].book_id
        return prev_book_id, next_book_id

    def add_author(self, author: Author):
        if author not in self.__authors:
            insort_left(self.__authors, author)
            self.__authors_index[author.unique_id] = author

    def get_author(self, author_id: int):
        author = None

        try:
            author = self.__authors_index[author_id]
        except KeyError:
            pass
        return author

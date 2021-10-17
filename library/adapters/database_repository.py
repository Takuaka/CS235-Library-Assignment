from typing import List

from sqlalchemy import desc, asc
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack

from library.domain.model import Book, Author, Publisher
from library.adapters.repository import AbstractRepository


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_session(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository):
    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def get_book(self, book_id: int):
        book = None
        try:
            book = self._session_cm.session.query(Book).filter(Book.book_id == id).one()
        except NoResultFound:
            pass
        return book

    def get_first_book_id(self):
        book = self._session_cm.session.query(Book).first()
        return book.book_id

    def get_last_book_id(self):
        book = self._session_cm.session.query(Book).order_by(desc(Book.book_id)).first()
        return book.book_id

    def add_book(self, book: Book):
        with self._session_cm as scm:
            scm.session.add(book)
            scm.commit()

    def get_prev_next_books_ids(self, book_id: int):
        prev_result = None
        prev_book = self._session_cm.session.query(Book).filter(Book._Book__id < book_id).order_by(desc(Book._Book__id)).first()
        if prev_book is not None:
            prev_result = prev_book.book_id

        next_result = None
        next_book = self._session_cm.session.query(Book).filter(Book._Book__id > book_id).order_by(asc(Book._Book__id)).first()
        if next_book is not None:
            next_result = next_book

        return prev_result, next_result

    def add_author(self, author: Author):
        with self._session_cm as scm:
            scm.session.add(author)
            scm.commit()

    def get_author(self, author_id:int):
        author = None
        try:
            author = self._session_cm.query(Author).filter(Author.unique_id == id).one()
        except NoResultFound:
            pass
        return author

    @property
    def books_list(self):
        pass

    @property
    def authors_list(self):
        pass

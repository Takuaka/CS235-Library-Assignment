import abc

from library.domain.model import Publisher, Author, Book

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_book(self, book_id: int):
        """Returns Book with id from Repository, return None if not there"""

        raise NotImplementedError

    @abc.abstractmethod
    def get_first_book_id(self):
        """Returns lowest book_id from Repository"""

        raise NotImplementedError

    @abc.abstractmethod
    def get_last_book_id(self):
        """Returns highest book_id from Repository"""

        raise NotImplementedError

    def add_book(self, book: Book):
        """adds a book to the Repository"""

        raise NotImplementedError

    def get_books_keys_list(self):
        """Returns a list of all the book IDs of books in repo"""

        raise NotImplementedError

    def get_books_dict(self):
        """Returns a dictionary of all the books in the repo"""

        raise NotImplementedError

    def get_prev_next_books(self, book_id: int):
        """returns 2 values; the book ID's of the two books that come directly before and after the current book ID"""

        raise NotImplementedError

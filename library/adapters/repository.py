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
    def get_first_book(self):
        """Returns Book with lowest id from Repository"""

        raise NotImplementedError

    @abc.abstractmethod
    def get_last_book(self):
        """Returns Book with highest id from Repository"""

        raise NotImplementedError

    def add_book(self, book: Book):
        """adds a book to the Repository"""

        raise NotImplementedError

#______________________________________________________________________________________

    @property
    @abc.abstractmethod
    def book_keys(self):
        """This property contains a list of the book ids; I will use it to iterate over for the book list"""

        raise NotImplementedError

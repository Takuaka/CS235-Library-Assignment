from typing import Iterable

from library.domain.model import Publisher, Author, Book
from library.adapters.repository import AbstractRepository


class NonExistentAuthorException(Exception):
    pass


def get_author_dict(repo: AbstractRepository):
    author_list = repo.authors_list
    services_dict = dict()
    for author in author_list:
        services_dict[author.unique_id] = author.full_name
    return services_dict


def get_author(author_id: int, repo: AbstractRepository):
    author = repo.get_author(author_id)
    if author is None:
        raise NonExistentAuthorException

    return author_to_dict(author)

####################################

# Author to Dict Conversion

####################################


def author_to_dict(author: Author):
    books = []
    if len(author.books) > 0:
        for book in author.books:
            books.append(book)

    coauthors = []
    if len(author.coauthors) > 0:
        for coauthor in author.coauthors:
            coauthors.append(coauthor)

    author_dict = {
        'author_full_name': author.full_name,
        'author_id': author.unique_id,
        'books': books,
        'coauthors': coauthors
    }
    return author_dict


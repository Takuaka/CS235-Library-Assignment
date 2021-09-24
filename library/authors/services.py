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

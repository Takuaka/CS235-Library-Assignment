import json
from pathlib import Path

from library.adapters.repository import AbstractRepository, RepositoryException
from library.domain.model import Publisher, Author, Book


class MemoryRepository(AbstractRepository):
    pass

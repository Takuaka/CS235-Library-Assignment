from pathlib import Path

from library.adapters.repository import AbstractRepository
from library.adapters.jsondatareader import BooksJSONReader


def populate(data_path: Path, repo: AbstractRepository, database_mode: bool):
    load_books(data_path, repo, database_mode)


def load_books(data_path: Path, repo: AbstractRepository, database_mode: bool):
    books_filename = str(data_path / "comic_books_excerpt.json")
    authors_filename = str(data_path / "book_authors_excerpt.json")
    books = BooksJSONReader(books_filename, authors_filename)
    books.read_json_files()
    for book in books.dataset_of_books:
        for author in book.authors:
            repo.add_author(author)
            author.add_book(book)
            for coauthor in book.authors:
                if coauthor != author:
                    author.add_coauthor(coauthor)
        repo.add_book(book)

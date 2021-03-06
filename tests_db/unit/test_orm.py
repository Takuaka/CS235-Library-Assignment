import pytest

from sqlalchemy.exc import IntegrityError

from library.domain.model import Publisher, Author, Book


def insert_publisher(empty_session):
    empty_session.execute(
        'INSERT INTO publisher (name) VALUES ("HarperCollins")'
    )
    row = empty_session.execute('SELECT name from publishers').fetchone()
    return row[0]


def insert_author(empty_session):
    empty_session.execute(
        'INSERT into authors (id, name) VALUES ("1425", "Scott Westerfield")'
    )
    row = empty_session.execute('SELECT id from authors').fetchone()
    return row[0]


def insert_book(empty_session):
    empty_session.execute(
        'INSERT into books (id, book_title, release_year, publisher, ebook, num_pages, description) VALUES ("4432", '
        '"The Secret Hour", "2004", "HarperCollins", "False", "297", "Test Description") '
    )
    row = empty_session.execute('SELECT id from books').fetchone()
    return row[0]


def insert_book_author_associations(empty_session, book_key, author_keys):
    stmt = 'INSERT INTO book_authors (book_id, author_id) VALUES (:book_id, :author_id)'
    for author_key in author_keys:
        empty_session.execute(stmt, {'book_id': book_key, 'author_id': author_key})


def make_book():
    book = Book(4432, "The Secret Hour")
    book.release_year = 2004
    book.publisher = Publisher("HarperCollins")
    book.ebook = False
    book.num_pages = 297
    book.description = "Test Description"

    return book


def make_author():
    author = Author(1425, "Scott Westerfield")

    return author


def make_publisher():
    publisher = Publisher("HarperCollins")

    return publisher


def test_loading_of_book(empty_session):
    book_key = insert_book(empty_session)
    expected_book = make_book()
    fetched_book = empty_session.query(Book).one()

    assert expected_book == fetched_book
    assert book_key == fetched_book.book_id


def test_loading_of_book_with_author_association(empty_session):
    book_key = insert_book(empty_session)
    author_keys = [insert_author(empty_session)]
    insert_book_author_associations(empty_session, book_key, author_keys)

    book = empty_session.query(Book).get(book_key)
    authors = [empty_session.query(Author).get(key) for key in author_keys]

    for author in authors:
        assert author in book.authors
        assert book in author.books

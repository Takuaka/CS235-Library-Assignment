from sqlalchemy import (
    Table, MetaData, Column, Integer, String, ForeignKey, Boolean
)

from sqlalchemy.orm import mapper, relationship, synonym

from library.domain import model

metadata = MetaData()

publisher_table = Table(
    'publishers', metadata,
    Column('name', String(255), primary_key=True, nullable=False)
)

author_table = Table(
    'authors', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False)
)

books_table = Table(
    'books', metadata,
    Column('id', Integer, primary_key=True),
    Column('book_title', String(255), nullable=False),
    Column('release_year', Integer),
    Column('publisher', ForeignKey('publishers.name')),
    Column('ebook', Boolean),
    Column('num_pages', Integer),
    Column('description', String(1024))
)

coauthors_table = Table(
    'coauthors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('author1', ForeignKey('authors.id')),
    Column('author2', ForeignKey('authors.id'))
)

author_books_table = Table(
    'book_authors', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('author', ForeignKey('authors.id')),
    Column('book', ForeignKey('books.id'))
)


def map_model_to_tables():
    mapper(model.Publisher, publisher_table, properties={
        '_Publisher__name': publisher_table.c.name
    })

    mapper(model.Author, author_table, properties={
        '_Author__name': author_table.c.name,
        '_Author__id': author_table.c.id
    })
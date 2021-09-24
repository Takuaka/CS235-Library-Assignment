from flask import Blueprint
from flask import request, render_template, url_for, session

import library.adapters.repository as repo
import library.authors.services as services

import library.books.services as book_services

authors_blueprint = Blueprint(
    'authors_bp', __name__)


@authors_blueprint.route('/authors', methods=['GET'])
def authors():
    authors_dict = services.get_author_dict(repo.repo_instance)
    return render_template(
        'authors/authors.html',
        authors_dict=authors_dict
    )


@authors_blueprint.route('/author_books/<author_id>', methods=['GET'])
def author_books(author_id):
    author = services.get_author(int(author_id), repo.repo_instance)
    books = []

    if len(author['books']) > 0:
        for book_id in author['books']:
            book = book_services.get_book(book_id, repo.repo_instance)
            books.append(book)

    return render_template(
        'authors/author_books.html',
        author_id=author['author_id'],
        author_name=author['author_full_name'],
        books=books
    )

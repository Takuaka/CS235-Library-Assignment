from flask import Blueprint
from flask import request, render_template, url_for, session

import library.adapters.repository as repo
import library.books.services as services

books_blueprint = Blueprint(
    'books_bp', __name__)


@books_blueprint.route('/books', methods=['GET'])
def books():
    book_dict = services.get_books_dict(repo.repo_instance)
    keys_list = services.get_keys_list(repo.repo_instance)
    return render_template(
        'books/books.html',
        book_dict=book_dict,
        keys_list=keys_list
    )


@books_blueprint.route('/book_details/<book_id>', methods=['GET'])
def book_details(book_id):
    book = services.get_book(int(book_id), repo.repo_instance)
    prev_book_id, next_book_id = services.get_prev_next_books_ids(int(book_id), repo.repo_instance)
    first_id, last_id = services.get_first_last_books_ids(repo.repo_instance)

    prev_book_url = None
    next_book_url = None
    first_book_url = None
    last_book_url = None

    if prev_book_id is not None:
        prev_book_url = url_for('books_bp.book_details', book_id=prev_book_id)
        first_book_url = url_for('books_bp.book_details', book_id=first_id)
    if next_book_id is not None:
        next_book_url = url_for('books_bp.book_details', book_id=next_book_id)
        last_book_url = url_for('books_bp.book_details', book_id=last_id)

    authors = ""
    authors_num = len(book['authors'])
    if authors_num > 1:
        i = 0
        while i < authors_num-1:
            authors = authors + book['authors'][i] + ", "
            i += 1
        authors = authors + book['authors'][authors_num-1]
    elif authors_num == 1:
        authors = book['authors'][0]
    else:
        authors = "Not Available"

    return render_template(
        'books/book_reviews.html',
        title=book['title'],
        book_id=book['book_id'],
        authors=authors,
        page_num=book['page_num'],
        publisher=book['publisher'],
        is_ebook=book['is_ebook'],
        description=book['description'],
        first_book_url=first_book_url,
        prev_book_url=prev_book_url,
        next_book_url=next_book_url,
        last_book_url=last_book_url
    )

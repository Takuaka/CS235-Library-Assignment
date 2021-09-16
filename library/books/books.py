from flask import Blueprint
from flask import request, render_template, url_for, session

import library.adapters.repository as repo
from library.utilities.services import book_to_dict, books_to_dict

books_blueprint = Blueprint(
    'books', __name__)


@books_blueprint.route('/books_list', methods=['GET'])
def books_list():
    return render_template(
        'books/books.html'

    )

# "image_url is what the direct link to an image of the book is found; looks icon size
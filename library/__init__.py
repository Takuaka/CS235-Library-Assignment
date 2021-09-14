"""Initialize Flask app."""

from pathlib import Path

from flask import Flask

import library.adapters.repository as repo
from library.adapters.memory_repository import MemoryRepository, populate

# TODO: Access to the books should be implemented via the repository pattern and using blueprints, so this can not stay here!
#from library.domain.model import Book

# TODO: Access to the books should be implemented via the repository pattern and using blueprints, so this can not stay here!
# def create_some_book():
#     some_book = Book(1, "Harry Potter and the Chamber of Secrets")
#     some_book.description = "Ever since Harry Potter had come home for the summer, the Dursleys had been so mean \
#                              and hideous that all Harry wanted was to get back to the Hogwarts School for \
#                              Witchcraft and Wizardry. But just as he’s packing his bags, Harry receives a \
#                              warning from a strange impish creature who says that if Harry returns to Hogwarts, \
#                              disaster will strike."
#     some_book.release_year = 1999
#     return some_book


# def create_app():
#     app = Flask(__name__)
#
#     @app.route('/')
#     def home():
#         some_book = create_some_book()
#         Use Jinja to customize a predefined html page rendering the layout for showing a single book.
        # return render_template('simple_book.html', book=some_book)
    #
    # return app

def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = Path('library') / 'adapters' / 'data'

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    with app.app_context():
        from .home import home
        app.register_blueprint (home.home_blueprint)

    return app
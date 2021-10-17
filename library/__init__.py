"""Initialize Flask app."""

from pathlib import Path

from flask import Flask

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from sqlalchemy.pool import NullPool

import library.adapters.repository as repo
from library.adapters import memory_repository, database_repository, repository_populate
from library.adapters.orm import metadata, map_model_to_tables


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = Path('library') / 'adapters' / 'data'

    if test_config is not None:
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

# Choosing either memory Repo or database Repo

    if app.config['REPOSITORY'] == 'memory':
        repo.repo_instance = memory_repository.MemoryRepository()
        database_mode = False
        repository_populate.populate(data_path, repo.repo_instance, database_mode)

    elif app.config['REPOSITORY'] == 'database':
        database_uri = app.config['SQLALCHEMY_DATABASE_URI']

        database_echo = app.config['SQLALCHEMY_ECHO']

        database_engine = create_engine(database_uri, connect_args={"check_same_thread": False}, poolclass=NullPool, echo=database_echo)

        session_factory = sessionmaker(autocommit=False, autoflush=True, bind=database_engine)

        repo.repo_instance = database_repository.SqlAlchemyRepository(session_factory)

        if app.config['TESTING'] == 'True' or len(database_engine.table_names()) == 0:
            print("REPOPULATING DATABASE...")
            # reinitialising database for testing or for first-time use of application
            clear_mappers()
            metadata.create_all(database_engine)
            for table in reversed(metadata.sorted_tables):
                database_engine.execute(table.delete())

            map_model_to_tables()

            database_mode = True
            repository_populate.populate(data_path, repo.repo_instance, database_mode)
            print("REPOPULATING DATABASE... FINISHED")

        else:
            map_model_to_tables()

    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .books import books
        app.register_blueprint(books.books_blueprint)

        from .authors import authors
        app.register_blueprint(authors.authors_blueprint)

        # These are for the database repo; not for the memory repo

        if app.config['REPOSITORY'] == 'database':

            @app.before_request
            def before_flask_http_request_function():
                if isinstance(repo.repo_instance, database_repository.SqlAlchemyRepository):
                    repo.repo_instance.reset_session()

            @app.teardown_appcontext
            def shutdown_session(exception=None):
                if isinstance(repo.repo_instance, database_repository.SqlAlchemyRepository):
                    repo.repo_instance.close_session()

    return app

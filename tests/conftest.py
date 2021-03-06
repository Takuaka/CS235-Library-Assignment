import pytest

from library import create_app
from library.adapters import memory_repository, repository_populate

from utils import get_project_root

TEST_DATA_PATH = get_project_root() / "tests" / "data"


@pytest.fixture
def in_memory_repo():
    repo = memory_repository.MemoryRepository()
    repository_populate.populate(TEST_DATA_PATH, repo)
    return repo


@pytest.fixture
def client():
    my_app = create_app({
        'TESTING': True,
        'REPOSITORY': 'memory',
        'TEST_DATA_PATH': TEST_DATA_PATH,
        # 'WTF_CSRF_ENABLED': False
    })

    return my_app.test_client()

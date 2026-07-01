import pytest
from pages.todo_page import TodoPage


@pytest.fixture
def todo_page(page):
    print("Setting up TodoPage fixture...")

    todo = TodoPage(page)
    todo.open()

    yield todo

    print("\nCleaning up TodoPage fixture...")

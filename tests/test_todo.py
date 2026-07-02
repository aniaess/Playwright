from playwright.sync_api import expect
from pages.todo_page import TodoPage


def test_add_todo(page):
    """
    Verify that a user can add multiple todo items successfully.

    Steps:
    1. Open TodoMVC application
    2. Add several todo items

    Expected result:
    - All added todo items are visible in the list
    """

    todo = TodoPage(page)

    todo.open_todo_app()

    # ADD
    todo.add_todo("Learn Playwright")
    todo.add_todo("Learn Python")
    todo.add_todo("Learn Pytest")

    expect(todo.todo_items).to_have_count(3)

    # COMPLETE
    todo.complete_todo("Learn Playwright")

    expect(
        todo.todo_items.nth(0).get_by_role("checkbox")
    ).to_be_checked()

    # ACTIVE FILTER
    todo.filter_active()
    expect(todo.todo_items).to_have_count(2)

    # COMPLETED FILTER
    todo.filter_completed()
    expect(todo.todo_items).to_have_count(1)

    # CLEAR COMPLETED
    todo.clear_completed()
    expect(todo.todo_items).to_have_count(0)

    # NEW DELETE STEP
    todo.filter_all()
    todo.add_todo("To be deleted")

    expect(todo.todo_items.filter(has_text="To be deleted")).to_be_visible()

    todo.delete_todo_by_text("To be deleted")
    expect(todo.todo_items).to_have_count(2)
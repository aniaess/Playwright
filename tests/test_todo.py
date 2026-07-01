from playwright.sync_api import expect


def test_add_todo(todo_page):
    """
    Verify that a user can add multiple todo items successfully.

    Steps:
    1. Open TodoMVC application
    2. Add several todo items

    Expected result:
    - All added todo items are visible in the list
    """

    # todo = TodoPage(page)
    #
    # todo.open()

    # ADD
    todo_page.add_todo("Learn Playwright")
    todo_page.add_todo("Learn Python")
    todo_page.add_todo("Learn Pytest")

    expect(todo_page.todo_items).to_have_count(3)

    # COMPLETE
    todo_page.complete_todo("Learn Playwright")

    expect(
        todo_page.todo_items.nth(0).get_by_role("checkbox")
    ).to_be_checked()

    # ACTIVE FILTER
    todo_page.filter_active()
    expect(todo_page.todo_items).to_have_count(2)

    # COMPLETED FILTER
    todo_page.filter_completed()
    expect(todo_page.todo_items).to_have_count(1)

    # CLEAR COMPLETED
    todo_page.clear_completed()
    expect(todo_page.todo_items).to_have_count(0)

    # NEW DELETE STEP
    todo_page.filter_all()
    todo_page.add_todo("To be deleted")

    expect(todo_page.todo_items.filter(has_text="To be deleted")).to_be_visible()

    todo_page.delete_todo_by_text("To be deleted")
    expect(todo_page.todo_items).to_have_count(2)
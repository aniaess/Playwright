from playwright.sync_api import expect


class TodoPage:
    """
       Page Object Model for the TodoMVC application.

       This class represents the main Todo page and provides methods to:
       - Add new todo items
       - Complete existing todos
       - Delete todos
       - Filter todos (Active / Completed / All)
       - Clear completed todos

       It encapsulates all interactions with the Todo list UI.
       """
    def __init__(self, page):

        self.page = page
        self.title = page.locator("h1")
        self.input_box = page.get_by_placeholder("What needs to be done?")
        self.todo_count = page.locator(".todo-count")
        self.todo_new_items = page.get_by_test_id("todo-title")
        self.todo_items = page.locator(".todo-list li")
        self.active_button = page.get_by_text("Active")
        self.completed_button = page.get_by_role("link", name="Completed")
        self.clear_completed_button = page.get_by_role("button", name="Clear completed")

    def open(self):
        """
            Opens the TodoMVC application.
        """
        self.page.goto("https://demo.playwright.dev/todomvc")

    def add_todo(self, text):
        """
            Adds a new todo item.
            Args:
                text (str): The text of the todo item.
        """
        self.input_box.fill(text)
        self.input_box.press("Enter")

    def complete_todo(self, text):
        """
        Marks a todo item as completed based on its visible text.
        Args:
            text (str): The text of the todo item to complete.
        """
        todo = self.page.locator(".todo-list li", has_text=text)
        todo.get_by_role("checkbox").check()

    def delete_todo_by_text(self, text):
        """
        Deletes a todo item based on its visible text.
        Args:
            text (str): Text of the todo item to delete.
        """
        todo = self.page.locator(".todo-list li", has_text=text)
        todo.hover()
        todo.locator("button.destroy").click()

    def filter_active(self):
        """
            Filters and shows only active (not completed) todos.
        """
        self.active_button.click()

    def filter_completed(self):
        """
            Filters and shows only completed todos.
        """
        self.completed_button.click()

    def clear_completed(self):
        """
        Removes all completed todo items from the list.
        """
        self.clear_completed_button.click()

    def filter_all(self):
        self.page.get_by_role("link", name="All").click()

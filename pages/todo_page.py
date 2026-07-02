from pages.base_page import BasePage
from utils.logger import logger


class TodoPage(BasePage):
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
    URL = "https://demo.playwright.dev/todomvc"

    def __init__(self, page):
        super().__init__(page)

        self.page = page
        self.title = page.locator("h1")
        self.input_box = page.get_by_placeholder("What needs to be done?")
        self.todo_count = page.locator(".todo-count")
        self.todo_new_items = page.get_by_test_id("todo-title")
        self.todo_items = page.locator(".todo-list li")
        self.active_button = page.get_by_text("Active")
        self.completed_button = page.get_by_role("link", name="Completed")
        self.clear_completed_button = page.get_by_role("button", name="Clear completed")
        self.all_button = page.get_by_role("link", name="All")

    def open_todo_app(self):
        """
            Opens the TodoMVC application.
        """
        logger.info("Opening Todo application")
        self.open(self.URL)

    def add_todo(self, text):
        """
            Adds a new todo item.
            Args:
                text (str): The text of the todo item.
        """
        logger.info(f"Adding todo: {text}")
        self.fill(self.input_box, text)
        self.input_box.press("Enter")

    def complete_todo(self, text):
        """
        Marks a todo item as completed based on its visible text.
        Args:
            text (str): The text of the todo item to complete.
        """
        logger.info(f"Completing todo: {text}")
        todo = self.page.locator(".todo-list li", has_text=text)
        todo.get_by_role("checkbox").check()

    def delete_todo_by_text(self, text):
        """
        Deletes a todo item based on its visible text.
        Args:
            text (str): Text of the todo item to delete.
        """
        logger.info(f"Deleting todo: {text}")
        todo = self.page.locator(".todo-list li", has_text=text)
        todo.hover()
        self.click(todo.locator("button.destroy"))


    def filter_active(self):
        """
            Filters and shows only active (not completed) todos.
        """
        logger.info("Filtering active todo items")
        self.click(self.active_button)

    def filter_completed(self):
        """
            Filters and shows only completed todos.
        """
        logger.info("Filtering completed todo items")
        self.click(self.completed_button)

    def clear_completed(self):
        """
        Removes all completed todo items from the list.
        """
        logger.info("Clearing completed todo items")
        self.click(self.clear_completed_button)

    def filter_all(self):
        """
           Displays all todo items.
        """
        logger.info("Displaying all todo items")
        self.click(self.all_button)
# TodoMVC Test Automation

This project contains automated UI tests for the TodoMVC application using Playwright and Pytest.

## Technologies

- Python
- Playwright
- Pytest
- Page Object Model (POM)

## Project Structure

```
TodoProject/
│
├── pages/
│   └── todo_page.py
│
├── tests/
│   ├── conftest.py
│   └── test_todo.py
│
├── .gitignore
├── README.md
├── requirements.txt
├── pytest.ini
└── .venv/
```
The .venv folder is not committed to Git because it is included in .gitignore.

## Installation

Clone the repository:

```bash
git clone <repository_url>
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Run Tests

```bash
pytest
```

## Test Coverage

The project demonstrates automated UI testing of the TodoMVC application, including:

- Adding todo items
- Completing todo items
- Filtering active todos
- Filtering completed todos
- Displaying all todos
- Clearing completed todos
- Deleting todo items

## Logging

The framework uses Python's built-in logging module to provide detailed execution logs.

Features
- Logs every important test action (e.g. opening the application, adding, completing and deleting todos)
- Automatically logs test start
- Automatically logs test result (PASSED / FAILED)
- Logs assertion errors and exceptions when a test fails
- Writes logs both to the console and to a log file
- Log file location: logs/test.log


## Design Pattern

The project follows the **Page Object Model (POM)** design pattern to improve readability, maintainability and reusability of test code.
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

## Design Pattern

The project follows the **Page Object Model (POM)** design pattern to improve readability, maintainability and reusability of test code.
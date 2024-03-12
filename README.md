# Expense Tracker

A simple web application for tracking expenses built with Flask.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

expense_tracker/
|-- app/
|   |-- __init__.py
|   |-- forms.py
|   |-- models.py
|   |-- routes.py
|   |-- static/
|   |   |-- styles.css
|   |-- templates/
|       |-- dashboard.html
|       |-- error.html
|       |-- layout.html
|       |-- login.html
|       |-- register.html
|-- venv/  (virtual environment)
|-- run.py
|-- config.py


## Introduction

Expense Tracker is a web application developed with Flask, a micro web framework for Python. The primary purpose of this project is to provide users with a platform to register, log in, and track their expenses. Users can view a dashboard displaying their recorded expenses.

## Project Structure

The project follows a structured organization to enhance readability and maintainability. The key components include:

- **app/**: Contains the Flask application and its components.
  - **__init__.py**: Initializes the Flask application.
  - **forms.py**: Includes WTForms for user registration and login.
  - **models.py**: Defines SQLAlchemy models (User, Expense).
  - **routes.py**: Handles routes and views.
  - **static/**: Holds static files such as stylesheets (`styles.css`).
  - **templates/**: Stores HTML templates for rendering views.
- **venv/**: Virtual environment to isolate dependencies.
- **run.py**: Script to run the Flask application.
- **config.py**: Configuration file for the Flask application.

## Requirements

- Python 3.x
- Flask
- Flask-WTF
- Flask-SQLAlchemy
- Flask-Login

## Installation

1. Clone the repository: `git clone https://github.com/Romeo509/personal-finance-tracker.git.
2. Navigate to the project folder: `cd expense-tracker`.
3. Create a virtual environment: `python -m venv venv`.
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`.

## Usage

1. Run the Flask application: `python run.py`.
2. Access the application in your web browser at `http://localhost:5000`.
3. Register a new account or log in if you already have one.
4. Use the dashboard to track your expenses.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).


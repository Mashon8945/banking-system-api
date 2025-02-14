# Banking System API

This is a banking system API built with Django and Django REST Framework. The API allows you to manage employees, customers, and transactions. It includes features for user authentication, customer management, and transaction processing.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Running Tests](#running-tests)
- [Docker Setup](#docker-setup)
- [Deployment](#deployment)
- [API Endpoints](#api-endpoints)

## Features

- User authentication (registration and login)
- Customer management (add, list, delete customers)
- Transaction processing (deposit and withdraw money)
- JWT authentication
- Dockerized for easy setup and deployment

## Requirements

- Python 3.9+
- Django 3.2+
- Django REST Framework
- PostgreSQL
- Docker (for containerization)
- Node.js and npm (for ESLint)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/mashon8945/banking-system-api.git
    cd banking-system-api
    ```

2. **Create and activate a virtual environment:**

    ```
    python -m venv venv
    `venv\Scripts\activate`
    ```

3. **Install the dependencies**

    ```
    pip install -r requirements.txt
    ```

4. **Set up the database**

    Ensure *PostgreSQL* is installed and running. Create a database and update the *DATABASE_URL* in ***settings.py***:
    ```
    DATABASES = {
        'default': dj_database_url.config(default='postgres://username:password@localhost:5432/banking_db')
    }
    ```

5. **Run Migrations**

    ```
    python manage.py migrate
    ```

6. **Create Superuser**

    ```
    python manage.py createsuperuser
    ```

**Running the Application**

    1. Start the development server:

        ```
        python manage.py runserver
        ```

    2. Access the application:

        (`http://127.0.0.1:8000/`)

**Running Tests**
    1. Run the test suite:

        ```
        python manage.py test
        ```

**Docker Setup**
    1. Build and run the Docker containers
        ```

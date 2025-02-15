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
- [Contributing](#contributing)
- [License](#license)

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

### 1. Clone the Repository

```sh
git clone https://github.com/mashon8945/banking-system-api.git
cd banking-system-api
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

### 4. Set Up the Database

Ensure *PostgreSQL* is installed and running. Create a database and update the *DATABASE_URL* in ***settings.py***:

```python
DATABASES = {
    'default': dj_database_url.config(default='postgres://username:password@localhost:5432/banking_db')
}
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

## Running the Application

### 1. Start the Development Server

```bash
python manage.py runserver
```

### 2. Access the Application

Open your browser and navigate to:

```
http://127.0.0.1:8000/
```

## Running Tests

### 1. Run the Test Suite

```bash
python manage.py test
```

## Docker Setup

### 1. Build and Run the Docker Containers

```bash
docker-compose build
docker-compose up
```

## Deployment

### 1. Create a DigitalOcean Droplet

- Go to the [DigitalOcean](https://www.digitalocean.com/) dashboard and create a new Droplet.
- Choose the Docker image from the marketplace.
- Configure the Droplet settings and create it.

### 2. SSH into the Droplet

```bash
ssh root@your_droplet_ip
```

### 3. Clone the Repository

```bash
git clone https://github.com/mashon8945/banking-system-api.git
cd banking-system-api
```

### 4. Build and Run the Docker Containers

```bash
docker-compose build
docker-compose up -d
```

### 5. Access the Application

Open your browser and navigate to:

```
http://your_droplet_ip:8000
```

## API Endpoints

### Authentication

- **Register:** `POST /api/employees/register`
- **Login:** `POST /api/employees/login`

### Customers

- **Add Customer:** `POST /api/customers/add`
- **List Customers:** `GET /api/customers`
- **Delete Customer:** `DELETE /api/customers/delete/<customer_id>`

### Transactions

- **Deposit Money:** `POST /api/transactions/deposit`
- **Withdraw Money:** `POST /api/transactions/withdraw`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the **MIT License**.


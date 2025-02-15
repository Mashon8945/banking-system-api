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
### Register Test

**Request:**

```
POST /api/employees/register
Content-Type: application/json
```

**Body:**

```json
{
    "username": "testuser",
    "email": "test@user.com",
    "password": "testpass",
    "role": "admin"
}
```

**Expected Response:**

```json
{
    "username": "testuser",
    "email": "test@user.com",
    "role": "admin"
}
```


- **Login:** `POST /api/employees/login`
### Login Test

**Request:**

```
POST /api/employees/login
Content-Type: application/json
```

**Body:**

```json
{
    "username": "testuser",
    "password": "testpass"
}
```

**Expected Response:**

```json
{
    "message": "Login successful"
}
```
### Obtain JWT Token

**Request:**

```
POST /api/token/
Content-Type: application/json
```

**Body:**

```json
{
    "username": "admin",
    "password": "testpass"
}
```
**Expected Response:**

```json
{
    "refresh": "<token>",
    "access": "<token>"
}
```

## Customers

### Add Customer

**Request:**

```
POST /api/customers/add
Authorization: Bearer <token>
Content-Type: application/json
```

**Body:**

```json
{
    "name": "Anto Goro",
    "email": "Goro@test.com",
    "account_balance": "2500.00"
}
```

**Expected Response:**

```json
{
    "name": "Anto Goro",
    "email": "Goro@test.com",
    "account_balance": "2500.00",
    "created_at": "2025-02-15T06:14:00.262488Z",
    "updated_at": "2025-02-15T06:14:00.262488Z"
}
```

### List Customers

**Request:**

```
GET /api/customers
Authorization: Bearer <token>
```

**Expected Response:**

```json
{
    "count": 4,
    "next": null,
    "previous": null,
    "results": [
        {
            "name": "Ann Terry",
            "email": "Annterry@test.com",
            "account_balance": "800.00",
            "created_at": "2025-02-14T10:59:37.854889Z",
            "updated_at": "2025-02-14T10:59:37.854889Z"
        },
        {
            "name": "Sim Simo",
            "email": "Simo@test.com",
            "account_balance": "950.00",
            "created_at": "2025-02-14T11:08:05.736750Z",
            "updated_at": "2025-02-14T11:08:05.736750Z"
        }
    ]
}
```

### Delete Customer

**Request:**

```
DELETE /api/customers/<customer_id>
```

**Expected Response:**

```json
{
    "message": "Customer deleted successful"
}
```


## Transactions

### Deposit Money

**Request:**

```
POST /api/transactions/deposit
Authorization: Bearer <token>
Content-Type: application/json
```

**Body:**

```json
{
    "customer": 4,
    "transaction_type": "deposit",
    "amount": "1200"
}
```

**Expected Response:**

```json
{
    "customer": 4,
    "transaction_type": "deposit",
    "amount": "1200"
}
```

### Withdraw Money

**Request:**

```
POST /api/transactions/withdraw
Authorization: Bearer <token>
Content-Type: application/json
```

**Body:**

```json
{
    "customer": 3,
    "transaction_type": "withdrawal",
    "amount": "1500.00"
}
```

**Expected Response:**

```json
{
    "customer": 3,
    "transaction_type": "withdrawal",
    "amount": "1500.00",
    "created_at": "2025-02-15T06:18:23.770982Z",
    "updated_at": "2025-02-15T06:18:23.770982Z"
}
```

## JWT Token Refresh

**Request:**

```
POST /api/token/refresh/
Authorization: Bearer <token>
Content-Type: application/json
```

**Expected Response:**

```json
{
    "access_token": "<token>"
}
```


- **Delete Customer:** `DELETE /api/customers/delete/<customer_id>`



## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the **MIT License**.


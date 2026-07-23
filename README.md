# 🛒 Mini E-Commerce Platform

A full-stack **Mini E-Commerce Platform** built with **Django**, **Django REST Framework**, **MySQL**, and **Bootstrap 5**.

The application provides both a modern HTML-based shopping website and a complete REST API with Swagger documentation.

---

# ✨ Features

## 👤 Authentication

- User Registration
- User Login
- User Logout
- Profile Management
- JWT Authentication (REST API)
- Django Session Authentication (Website)

---

## 📦 Product Management

- Product Listing
- Product Details
- Featured Products
- Category Filtering
- Product Search
- Product Images
- Stock Management

---

## 🛍 Shopping Cart

- Add Product to Cart
- Update Quantity
- Remove Product
- Cart Total
- Cart Badge Counter

---

## 💳 Checkout

- Shipping Address
- Cash on Delivery
- Order Summary
- Stock Validation
- Automatic Stock Reduction
- Cart Clearance after Checkout

---

## 📄 Orders

- Order History
- Order Details
- Order Status

---

## 👨‍💼 Admin Panel

Admin can manage:

- Users
- Categories
- Products
- Orders
- Order Items

---

## 🌐 REST API

Complete REST APIs built using Django REST Framework.

- Authentication
- Categories
- Products
- Shopping Cart
- Orders

Swagger documentation included.

---

# 🛠 Tech Stack

## Backend

- Python 3.11
- Django 5
- Django REST Framework
- Simple JWT

## Frontend

- HTML5
- CSS3
- Bootstrap 5
- Bootstrap Icons

## Database

- MySQL

## Documentation

- Swagger (drf-yasg)

---

# 📂 Project Structure

```
Mini-Ecommerce/

│── accounts/
│── cart/
│── categories/
│── config/
│── core/
│── orders/
│── products/
│── templates/
│── static/
│── media/
│── manage.py
│── requirements.txt
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/biradarvivek/Supremus_Angel_TechAssignment.git

cd Supremus_Angel_TechAssignment
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Requirements

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

Example:

```env
SECRET_KEY=your-secret-key

DEBUG=True

DB_NAME=ecommerce

DB_USER=root

DB_PASSWORD=yourpassword

DB_HOST=localhost

DB_PORT=3306
```

---

## Run Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## Create Superuser

```bash
python manage.py createsuperuser
```

---

## Start Server

```bash
python manage.py runserver
```

Application

```
http://127.0.0.1:8000/
```

---

# 🔑 REST API Endpoints

## Authentication

| Method | Endpoint |
|----------|----------------------------|
| POST | `/api/auth/register/` |
| POST | `/api/auth/login/` |
| POST | `/api/auth/refresh/` |
| POST | `/api/auth/logout/` |
| GET | `/api/auth/profile/` |

---

## Categories

| Method | Endpoint |
|----------|----------------------------|
| GET | `/api/categories/` |
| POST | `/api/categories/` |
| GET | `/api/categories/{id}/` |
| PUT | `/api/categories/{id}/` |
| DELETE | `/api/categories/{id}/` |

---

## Products

| Method | Endpoint |
|----------|----------------------------|
| GET | `/api/products/` |
| POST | `/api/products/` |
| GET | `/api/products/{id}/` |
| PUT | `/api/products/{id}/` |
| DELETE | `/api/products/{id}/` |

Supports:

- Search
- Filtering
- Ordering
- Pagination

---

## Shopping Cart

| Method | Endpoint |
|----------|----------------------------|
| GET | `/api/cart/` |
| POST | `/api/cart/add/` |
| PATCH | `/api/cart/items/{id}/` |
| DELETE | `/api/cart/items/{id}/delete/` |

---

## Orders

| Method | Endpoint |
|----------|----------------------------|
| POST | `/api/orders/checkout/` |
| GET | `/api/orders/` |
| GET | `/api/orders/{id}/` |

---

# 📖 API Documentation

Swagger

```
http://127.0.0.1:8000/swagger/
```

ReDoc

```
http://127.0.0.1:8000/redoc/
```

---

# 📸 Media Upload

Product Images

```
media/products/
```

Profile Images

```
media/profiles/
```

---

# 📄 License

This project was developed as part of a technical assessment for educational and evaluation purposes.

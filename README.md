
# Secure RESTful API

This project is a secure RESTful API built using **Flask**, **JWT**, and **SQLite** for managing users and products. It was developed as part of an **Information Security Management** course to demonstrate best practices in authentication, authorization, and secure API development.

---

## 🔐 Features

- JWT-based authentication
- Secure password hashing using Werkzeug
- CRUD operations for users and products
- Token-protected routes
- Environment-based configuration using `.env`

---

## 🛠️ Tech Stack

- Python
- Flask
- SQLite (via SQLAlchemy)
- Flask-JWT-Extended
- Python-Dotenv

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git https://github.com/manarelmaradny/secure-restful-api.git
cd secure-restful-api
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

Create a `.env` file in the root directory with the following content:

```env
SECRET_KEY=your_secret_key_here
DATABASE_URI=sqlite:///site.db
```


### 5. Run the App

```bash
python app.py
```

The API will be available at `http://127.0.0.1:5000/`

---

## 📁 Project Structure

```
secure-restful-api/
├── app.py             # Main application file
├── config.py          # Loads environment variables
├── models.py          # Database models for User and Product
├── routes.py          # All API endpoints
├── requirements.txt   # Python dependencies
├── .env               # contains secret keys & DB URI
```

---

## 📌 API Endpoints

### 🔐 Authentication

- `POST /signup` – Register a new user
- `POST /login` – Login and receive a JWT token (valid for 10 minutes)

### 👤 User Operations

- `PUT /users/<id>` – Update user info (Requires token)

### 📦 Product Operations (Require JWT Token)

- `POST /products` – Add a product
- `GET /products` – View all products
- `GET /products/<pid>` – View product by ID
- `PUT /products/<pid>` – Update product
- `DELETE /products/<pid>` – Delete product

---

## 🔒 Security Best Practices

- Passwords are securely hashed using Werkzeug
- JWT token required for all sensitive routes
- Secret keys and database info stored in `.env`
- Routes protected using `@jwt_required()`

---

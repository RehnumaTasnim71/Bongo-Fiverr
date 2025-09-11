
# Bongo-Fiverr (Django)

A Django-based freelancer marketplace platform where **buyers** can hire services, place orders, and leave reviews, while **sellers** can manage their services, track earnings, and view customer feedback.

---

## ✨ Features

### 👥 User Management
- Custom user model with **Buyer** & **Seller** roles.
- Secure authentication (signup, login, logout).
- Profile management with editable user details.

### 📦 Services & Orders
- Sellers can **create & manage services**.
- Buyers can **place service orders**.
- Order tracking with status updates (`pending`, `completed`, etc.).

### ⭐ Reviews & Ratings
- Buyers can submit **reviews** for completed orders
- Reviews include **rating + comment**
- Sellers can view all reviews in their dashboard

### 💰 Seller Dashboard
- List of all posted services.
- Orders received from buyers.
- **Total earnings** from completed orders.
- Reviews received from buyers.

### 📖 API Documentation
- **Swagger/OpenAPI** auto-generated documentation available at: http://127.0.0.1:8000/swagger/

## ⚙️ Installation Guide

**Clone the repository**
   ```bash
   git clone https://github.com/RehnumaTasnim71/Bongo-Fiverr.git
   cd Bongo-Fiverr

## Quick Start
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Open http://127.0.0.1:8000/
- Register as Buyer/Seller to test
- Seller can post services, Buyer can place orders, complete order -> Buyer leaves review

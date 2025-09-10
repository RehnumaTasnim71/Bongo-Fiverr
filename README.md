
# Freelancer Platform (Django)

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

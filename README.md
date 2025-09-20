# Healthcare Backend

A Django REST Framework (DRF) backend for a healthcare management system. This project provides APIs for user authentication, managing patients, doctors, and patient-doctor mappings with JWT authentication and PostgreSQL integration.

---

## Features

- User registration and JWT-based authentication
- CRUD operations for Patients and Doctors
- Assign doctors to patients
- PostgreSQL database integration
- Secure and modular design using Django REST Framework
- Admin dashboard for managing all entities

---

## Tech Stack

- Python 3.12
- Django 5.x
- Django REST Framework
- PostgreSQL
- djangorestframework-simplejwt (JWT authentication)

---

## Project Structure

healthcare_backend/
├── accounts/ # User authentication app
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
├── patients/ # Patient and doctor management app
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ └── urls.py
├── healthcare_backend/ # Django project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
└── requirements.txt

##
## Installation

1. Clone the repository:

```bash
git clone https://github.com/Piyanshu129/Healthcare-Backend.git
cd Healthcare-Backend

python3 -m venv .venv
source .venv/bin/activate


pip install -r requirements.txt
```

## .env::--
```
DEBUG=True
SECRET_KEY=your_secret_key
DB_NAME=healthdb
DB_USER=healthuser1
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

## run migrations:
```
python manage.py makemigrations
python manage.py migrate
```

## Create a superuser for admin access:
```python manage.py createsuperuser```

## Start the development server:
```python manage.py runserver```

---

## API Endpoints
1.Authentication

- POST /api/auth/register/ – Register a new user
- POST /api/auth/login/ – Login and obtain JWT tokens

2.Patients

- POST /api/patients/ – Create a new patient
- GET /api/patients/ – Retrieve all patients
- GET /api/patients/<id>/ – Retrieve a single patient
- PUT /api/patients/<id>/ – Update patient details
- DELETE /api/patients/<id>/ – Delete a patient

3.Doctors

- POST /api/doctors/ – Create a new doctor
- GET /api/doctors/ – Retrieve all doctors
- GET /api/doctors/<id>/ – Retrieve a single doctor
- PUT /api/doctors/<id>/ – Update doctor details
- DELETE /api/doctors/<id>/ – Delete a doctor

4.Patient-Doctor Mapping

- POST /api/mappings/ – Assign a doctor to a patient
- GET /api/mappings/ – List all mappings
- GET /api/mappings/<patient_id>/ – List doctors for a patient
- DELETE /api/mappings/<id>/ – Remove a doctor from a patient

---


## Testing with Postman

- Register a user (/api/auth/register/)

- Login to get JWT tokens (/api/auth/login/)

- Add JWT token in Postman Authorization → Bearer Token

- Test patient, doctor, and mapping endpoints






# SyncPulse

SyncPulse is a backend project built with Django and Django REST Framework.

The goal of this project is to learn how production backend systems are designed by implementing authentication, organization management, project tracking, notifications, background jobs, real-time communication, and third-party integrations.

The project is being built step by step while following backend engineering best practices.

---

## Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication
- Git & GitHub

---

## Features Completed

### Project Setup

- Django project initialization
- PostgreSQL configuration
- Environment variables
- Requirements management

### User Management

- Custom User Model
- UUID Primary Keys
- Shared BaseModel

### Organization Module

- Organization model
- Organization members
- Role management (Admin, Manager, Member)
- Automatic slug generation

### Authentication

- Custom User Model
- User Registration API
- JWT Login API
- Refresh Token API
- Current User API
- JWT Logout with Token Blacklisting

---

## Next

- Profile API
- Password Change
- Logout
- Project Management Module

---

## Running the Project

```bash
git clone https://github.com/Anjali470/syncpulse.git

cd syncpulse

python -m venv venv

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
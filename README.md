# SyncPulse 🚀

A production-inspired backend project built with **Django** and **Django REST Framework** to simulate a real-time team productivity platform.

The goal of this project is to learn and implement production-level backend concepts including authentication, multi-tenancy, real-time communication, background jobs, AI integration, caching, testing, Docker, and deployment.

> **Project Status:** 🚧 Under Development

---

## Tech Stack

- Python 3.11+
- Django 5
- Django REST Framework
- PostgreSQL
- python-dotenv
- Git & GitHub

---

## Current Progress

### ✅ Project Initialization

- Django project setup
- Modular app architecture
- Environment configuration using `.env`
- PostgreSQL integration
- GitHub repository initialized

### ✅ Authentication Foundation

- Custom User Model using `AbstractUser`
- Configured `AUTH_USER_MODEL`
- Initial database migrations

---

## Project Structure

```
syncpulse/
│
├── accounts/          # Authentication & User Management
├── organizations/     # Multi-tenant organizations
├── boards/            # Projects, Sprints & Tasks
├── notifications/     # User notifications
├── jobs/              # Celery background jobs
├── integrations/      # GitHub & third-party integrations
├── ai/                # AI Sprint Coach
├── common/            # Shared utilities and base models
│
├── syncpulse/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .env.example
```

---

## Learning Objectives

This project is being built to gain hands-on experience with:

- Django REST Framework
- JWT Authentication
- Role-Based Authorization
- PostgreSQL
- Django Channels (WebSockets)
- Redis
- Celery
- Docker
- AI Integration (Gemini API)
- GitHub Webhooks
- CI/CD
- Testing with Pytest

---

## Development Roadmap

- [x] Initialize Django project
- [x] Configure PostgreSQL
- [x] Create Custom User Model
- [ ] Organization & Membership System
- [ ] JWT Authentication
- [ ] Role-Based Permissions
- [ ] Project & Sprint APIs
- [ ] Task Management APIs
- [ ] Nested Serializers
- [ ] Filtering & Pagination
- [ ] WebSocket Integration
- [ ] Redis
- [ ] Celery
- [ ] AI Sprint Coach
- [ ] GitHub Webhooks
- [ ] Notifications
- [ ] Docker
- [ ] Testing
- [ ] Deployment

---

## Getting Started

### Clone the repository

```bash
git clone https://github.com/Anjali470/syncpulse.git
cd syncpulse
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=syncpulse
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server

```bash
python manage.py runserver
```

---

## Current Milestone

✔ Django project initialized

✔ PostgreSQL configured

✔ Custom User Model implemented

---

## Upcoming Milestone

Organization & Multi-Tenant Architecture

---

## Author

**Anjali Kummara**

Backend Developer | Python | Django | Django REST Framework

Currently building production-inspired backend systems to strengthen backend engineering skills.
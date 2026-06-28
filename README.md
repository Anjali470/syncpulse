# SyncPulse 

A production-inspired backend platform built with **Django** and **Django REST Framework** that simulates a real-time team productivity and collaboration system.

SyncPulse is designed to mimic how modern SaaS platforms like **Jira**, **ClickUp**, **Asana**, and **Monday.com** manage organizations, projects, tasks, notifications, and real-time collaboration.

The objective of this project is to gain hands-on experience with production-ready backend development by implementing authentication, multi-tenancy, REST APIs, real-time communication, background processing, AI integration, testing, and deployment.

> **Project Status:**  Under Active Development

---

# Tech Stack

### Backend

 Python 3.11+
 Django 5
 Django REST Framework

### Database

 PostgreSQL

### Environment Management

 python-dotenv

### Version Control

 Git
 GitHub

---

# Current Progress

##  Project Foundation

 Django project initialized
 Modular app architecture
 PostgreSQL configured
 Environment variable configuration using `.env`
 Requirements management
 Project documentation

---

##  Authentication Foundation

 Custom User Model using `AbstractUser`
 UUID-based primary keys
 Shared `BaseModel`
 Email-based authentication configuration
 Django Admin integration

---
 User Registration API
 Login API using JWT
 Access Token generation
 Refresh Token generation
 SimpleJWT integration
 DRF authentication configuration

## JWT Authentication


##  Multi-Tenant Organization Module

- Organization model
- Automatic slug generation
- Organization ownership
- Organization Member model
- Role-based membership

  - Admin
  - Manager
  - Member
- Membership constraints to prevent duplicate users in an organization

---

# Project Structure

```text
syncpulse/

├── accounts/          # Custom User & Authentication
├── organizations/     # Organizations & Memberships
├── boards/            # Projects, Sprints & Tasks
├── notifications/     # Notification Service
├── jobs/              # Celery Background Jobs
├── integrations/      # GitHub & Third-party Integrations
├── ai/                # AI Sprint Coach
├── common/            # Shared Base Models & Utilities

├── syncpulse/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py

├── requirements.txt
├── README.md
├── manage.py
└── .env.example
```

---

# Database Design (Current)

```text
User
 │
 │ owns
 ▼
Organization
 │
 │
 ▼
OrganizationMember
```

The application follows a **multi-tenant architecture**, where each organization maintains its own members, projects, and resources independently.

---

# Learning Objectives

This project is being built to gain practical experience with:

 Django REST Framework
 JWT Authentication
 Role-Based Authorization
 PostgreSQL
 Django Channels (WebSockets)
 Redis
 Celery
 Docker
 AI Integration (Gemini API)
 GitHub Webhooks
 Performance Optimization
 Testing with Pytest
 CI/CD Pipelines

---

# Development Roadmap

## Foundation

 [x] Initialize Django Project
 [x] Configure PostgreSQL
 [x] Configure Environment Variables
 [x] Create Shared BaseModel
 [x] Create Custom User Model

## Organization Module

 [x] Organization Model
 [x] Organization Membership
 [x] Role Management

## Authentication

 [x] JWT Authentication
 [x] Login API
 [ ] Registration API
 [ ] Refresh Tokens
 [ ] Logout

## Project Management

 [ ] Project APIs
 [ ] Sprint APIs
 [ ] Task APIs
 [ ] Labels
 [ ] Comments
 [ ] Attachments

## API Features

 [ ] Nested Serializers
 [ ] Filtering
 [ ] Searching
 [ ] Ordering
 [ ] Pagination

## Real-Time

 [ ] Django Channels
 [ ] WebSocket Notifications
 [ ] Live Task Board

## Background Processing

 [ ] Celery
 [ ] Celery Beat
 [ ] Email Notifications

## AI

 [ ] Gemini AI Sprint Coach
 [ ] AI Stand-up Summary

## Integrations

 [ ] GitHub Webhooks
 [ ] Activity Logs

## Deployment

 [ ] Docker
 [ ] GitHub Actions
 [ ] Railway Deployment

## Testing

 [ ] Unit Testing
 [ ] API Testing
 [ ] WebSocket Testing

---

# Getting Started

## Clone Repository

```bash
git clone https://github.com/Anjali470/syncpulse.git
cd syncpulse
```

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file.

```env
SECRET_KEY=your_secret_key

DEBUG=True

DB_NAME=syncpulse
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

## Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Create Superuser

```bash
python manage.py createsuperuser
```

## Run Development Server

```bash
python manage.py runserver
```

---

# Current Milestone

 Project Foundation

 Authentication Foundation

 Organization & Membership Module

---

# Upcoming Milestone

 JWT Authentication & User APIs

---

# Author

**Anjali Kummara**

Backend Developer | Python | Django | Django REST Framework

Currently building production-inspired backend systems while learning scalable backend architecture, real-time communication, distributed systems, AI integrations, and cloud-ready development.

# helpdesk_api_project
Helpdesk Complaint Management API

A RESTful API built with Django and Django REST Framework to manage complaints/tickets. The system allows users to create, track, update, and filter complaints with authentication and pagination support.

Features
1.JWT Authentication (Login & Token refresh)

2.Create complaints

3.List complaints with pagination

4.Filter by category, priority, and status

5.Update complaint status

6.Delete complaints

7.Automatic timestamps (created_at, updated_at)

Tech Stack
Backend: Django 5.x

API Framework: Django REST Framework

Database: PostgreSQL

Authentication: JWT (SimpleJWT)

Filtering: django-filter

Project Structure
helpdesk_api_project/ │ ├── ticketraiser/ │ ├── settings.py │ ├── urls.py │ ├── complaint/ │ ├── models.py │ ├── serializers.py │ ├── views.py │ ├── migrations/ │ ├── manage.py

Installation & Setup
1️. Clone repository 2️. Create virtual environment python -m venv env env\Scripts\activate # Windows 3️. Install dependencies 4️. Configure database

-> Update settings.py with your PostgreSQL credentials:

DATABASES = { 'default': { 'ENGINE': 'django.db.backends.postgresql', 'NAME': 'your_db_name', 'USER': 'postgres', 'PASSWORD': 'your_password', 'HOST': 'localhost', 'PORT': '5432', } } 5️. Apply migrations python manage.py makemigrations python manage.py migrate 6️. Create superuser python manage.py createsuperuser 7️. Run server python manage.py runserver

API will be available at:

http://127.0.0.1:8000/

Authentication
Obtain JWT Token POST /api/token/

Body:

{ "username": "yourusername", "password": "yourpassword" }

Use token in headers:

Authorization: Bearer <access_token>

API Endpoints
-> Complaints Method Endpoint Description GET /complaints/ List complaints POST /complaints/ Create complaint GET /complaints// Retrieve complaint PUT /complaints// Update complaint PATCH /complaints// Partial update DELETE /complaints// Delete complaint

Filtering & Pagination
Filter examples /complaints/?category=network /complaints/?priority=high /complaints/?status=open Pagination /complaints/?page=2

Complaint Model
title: CharField description: TextField category: classroom | hostel | network priority: low | medium | high status: open | in-progress | closed created_at: DateTime updated_at: DateTime

Example Request
Create Complaint POST /complaints/

{ "title": "WiFi not working", "description": "Internet down in hostel", "category": "network", "priority": "high" }

Future Improvements
Role-based permissions (Admin / User)

Email notifications

Complaint dashboard analytics

File attachments support

Swagger API documentation

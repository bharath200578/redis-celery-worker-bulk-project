# Async Task Processing with Django, Celery & Redis

A robust asynchronous task processing system designed to handle long-running operations (like bulk data imports, PDF report generation, or heavy analytics) without blocking the main web server.

## Overview
This project demonstrates how to offload resource-intensive tasks from the HTTP request-response cycle using Celery as the task queue and Redis as the message broker.

## Key Features
* **Non-Blocking Architecture:** Immediate HTTP response for heavy tasks.
* **Persistent Task Tracking:** Uses Django models to track the status (`PENDING`, `PROCESSING`, `SUCCESS`, `FAILURE`) of background jobs.
* **Real-time Monitoring:** API endpoints to poll and verify the status of individual tasks.
* **Windows-Compatible:** Configured for development on Windows using the `solo` pool executor.

## Prerequisites
* Python 3.x
* [Redis](https://redis.io/) (installed and running locally)

## Installation & Setup

1. **Install dependencies:**
   ```bash
   pip install celery redis django-celery-results

Configure Django (settings.py):
Ensure CELERY_BROKER_URL and CELERY_RESULT_BACKEND are set to redis://127.0.0.1:6379/0.

Database Migration:

Bash
python manage.py makemigrations
python manage.py migrate

Running the Project
Open three terminal windows to run the required services:

Start Redis Server:

Bash
redis-server
Start Celery Worker (Windows specific fix):

Bash
celery -A my_project worker --pool=solo --loglevel=info
Start Django Server:

Bash
python manage.py runserver
API Usage
Trigger a Task: GET /api/reports/generate/

Returns: { "message": "...", "report_id": 1, "task_id": "..." }

Check Status: GET /api/reports/status/<report_id>/

Returns: Current task status and completion progress.
"""


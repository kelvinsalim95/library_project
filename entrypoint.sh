#!/bin/sh

# Start your Django application (e.g., using Gunicorn)
exec gunicorn --bind 0.0.0.0:8000 library_project.wsgi:application
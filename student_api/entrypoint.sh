#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# If a database host is defined, wait for it using a quick Python socket loop
if [ -n "$DB_HOST" ] && [ -n "$DB_PORT" ]; then
    echo "Waiting for database at $DB_HOST:$DB_PORT..."
    python -c "
import socket, sys, time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for _ in range(60):
    try:
        s.connect(('$DB_HOST', int('$DB_PORT')))
        print('Database is online!')
        sys.exit(0)
    except Exception:
        time.sleep(1)
print('Database check timed out!')
sys.exit(1)
"
fi

# Run migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn server
echo "Starting Gunicorn server..."
exec gunicorn student_api.wsgi:application --bind 0.0.0.0:8000

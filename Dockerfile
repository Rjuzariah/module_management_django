# Use official Python image
FROM python:3.12

# Set the working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run migrations
RUN python manage.py migrate

# Expose port 8000
EXPOSE 8000

# Start the Django app using Gunicorn
CMD ["gunicorn", "modular_system.wsgi:application", "--bind", "0.0.0.0:8000"]

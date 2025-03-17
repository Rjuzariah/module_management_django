# Django Project Setup and Running Instructions

This guide will help you set up and run the Django project, starting from database migrations to running the development server.

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.x
- pip (Python's package installer)
- Django
- A Database (PostgreSQL, MySQL, SQLite, etc.)

## 1. Clone the Repository

Start by cloning the project repository to your local machine:

```bash
git clone https://github.com/your-repository.git
cd your-repository

## 2. Clone the Repository

Start by cloning the project repository to your local machine:

```bash
git clone https://github.com/your-repository.git
cd your-repository

## 3. Set Up Virtual Environment

It’s recommended to create a virtual environment to manage your project’s dependencies:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

## 4. Install Dependencies

Once your virtual environment is set up, install all the required dependencies for the project using `pip`. This will ensure you have all the necessary packages for the project to run smoothly.

Run the following command to install dependencies:

```bash
pip install -r requirements.txt

## 5. Database Migrations

Run this following command if you have new update to the model
````bash
python manage.py makemigrations

To apply migrations and create the necessary tables in your database:
````bash
python manage.py migrate

## 6.Run the Development Server
To run the Django development server, use the following command:
````bash
python manage.py runserver



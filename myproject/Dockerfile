# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client

# Install project dependencies
RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variables for PostgreSQL connection
ENV POSTGRES_DB=mydbname \
    POSTGRES_USER=mydbuser \
    POSTGRES_PASSWORD=mydbpassword \
    POSTGRES_HOST=db \
    POSTGRES_PORT=5432

# Wait for PostgreSQL to be ready before running the application
CMD ["sh", "-c", "while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do sleep 1; done; python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

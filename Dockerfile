# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

RUN pip install --upgrade pip

# Install required libraries
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

RUN apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    libtiff-dev \
    libfreetype6-dev \
    libwebp-dev \
    libffi-dev \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app


# Copy the requirements file into the container at /app
COPY ./src/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY ./src /app/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "approot.wsgi:application"]

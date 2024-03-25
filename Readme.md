# Restaurant Review Platform

## Overview

The Restaurant Review Platform is a web application built with Django and Django REST Framework. It enables users to view a list of restaurants, post reviews, and rate them. The application provides RESTful APIs and is containerized with Docker for easy setup and deployment.

## Features

- View list of restaurants and detailed information about each.
- User authentication system for secure access and user management.
- Users can post reviews and rate restaurants.
- Integration with external map APIs to display restaurant locations.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- Docker and Docker Compose (for container management)

### Local Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/MaksatNiiazov/TataDev-TestTask.git
   cd restaurant-reviews
Install the dependencies:


pip install -r requirements.txt
Run database migrations:


python manage.py migrate
###Start the development server:

python manage.py runserver
The application will be available at http://localhost:8000.

###Using Docker
Build the Docker image:

docker-compose build

###Start the Docker containers:

docker-compose up

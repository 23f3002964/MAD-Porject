# Vehicle Parking Web App

## Description

A Django-based web application for managing and viewing vehicle parking spots. This application allows users to see a list of currently available parking spots, including their location, size, and unique identifier.

## Prerequisites

To run this project, you will need:

*   Python 3.10+
*   Django 5.2+
*   Pip (Python package installer)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    ```
    (Replace `<your-repository-url>` with the actual URL of the repository)

2.  **Navigate to the project directory:**
    ```bash
    cd parking_project
    ```

3.  **Install dependencies:**
    Currently, the main dependency is Django.
    ```bash
    pip install Django~=5.2
    ```
    (In the future, this might be replaced by `pip install -r requirements.txt` if a requirements file is added.)

4.  **Apply database migrations:**
    This command sets up the database schema based on the models defined.
    ```bash
    python manage.py migrate
    ```

5.  **Populate initial data:**
    This command loads some initial parking spot data into the database using a custom management command.
    ```bash
    python manage.py populate_spots
    ```

## Running the Application

1.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```

2.  **Access the application:**
    Open your web browser and navigate to:
    `http://127.0.0.1:8000/parking/available-spots/`

    You should see a list of parking spots that are currently available.

## Running Tests

To ensure the application is working correctly, you can run the unit tests for the `parking` app:

```bash
python manage.py test parking
```

This command will execute all tests defined in `parking/tests.py`.

## Project Structure

The project is organized as follows:

```
parking_project/          # Root directory of the checkout
├── manage.py             # Django's command-line utility for project management
├── parking/              # The 'parking' application, containing parking-specific logic
│   ├── __init__.py
│   ├── admin.py          # Admin site configurations (if any)
│   ├── apps.py           # Application configuration for 'parking'
│   ├── management/       # Custom Django management commands
│   │   └── commands/
│   │       └── populate_spots.py # Command to add initial parking spot data
│   ├── migrations/       # Database migration files for the 'parking' app
│   ├── models.py         # Data models (e.g., ParkingSpot)
│   ├── static/           # Static files (CSS, JavaScript, images) for 'parking' app
│   │   └── parking/
│   │       └── style.css # Stylesheet for the parking app
│   ├── templates/        # HTML templates for the 'parking' app
│   │   └── parking/
│   │       └── available_spots_list.html # Template to display available spots
│   ├── tests.py          # Unit tests for the 'parking' app
│   ├── urls.py           # URL routing for the 'parking' app
│   └── views.py          # View functions or classes for handling requests
├── parking_project/      # Main Django project configuration directory
│   ├── __init__.py
│   ├── asgi.py           # ASGI config for asynchronous web servers
│   ├── settings.py       # Django project settings
│   ├── urls.py           # Project-level URL routing
│   └── wsgi.py           # WSGI config for synchronous web servers
└── README.md             # This file
```
(Note: Some files like `db.sqlite3` or `__pycache__` directories are omitted for brevity.)

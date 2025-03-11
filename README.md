# Workout Tracker

This is a simple workout tracking web application built using Django. Users can register, log in, track exercises, and view their exercise history.

## Features
- User authentication (Login/Register/Logout)
- Dashboard to view logged exercises
- Form to track new exercises

## Technologies Used
- Django (Backend framework)
- Bootstrap (Frontend styling)
- SQLite (Default database)

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/exercise-tracker.git
   cd exercise-tracker
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```sh
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`

## Usage
- Register a new account
- Log in to the dashboard
- Track your exercises with reps, sets, and weight
- View your logged exercises
- Logout when finished

## Project Structure
```
exercise-tracker/
│── exercisehq/          # Main Django project folder
│── templates/           # HTML templates
│── static/              # CSS, JS, and images
│── db.sqlite3           # Database
│── manage.py            # Django management script
└── README.md            # Project documentation
```

## License
This project is licensed under the MIT License.

# Exercise Tracker

An Exercise Tracking App built using Django that allows users to register, log in, and track their workouts privately.

## Features
- User authentication (registration & login)
- Add, edit, and delete exercise logs
- Track exercise details including name, reps, sets, and weight
- Responsive and user-friendly UI

## Tech Stack
- **Backend:** Django, SQLite
- **Frontend:** HTML, CSS, Bootstrap
- **Version Control:** Git & GitHub

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/exercise-tracker.git
   cd exercise-tracker
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
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
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Run the server:
   ```sh
   python manage.py runserver
   ```
7. Open in browser:
   ```
   http://127.0.0.1:8000/
   ```

## Usage
- Register/Login to your account
- Add exercises with details (name, reps, sets, weight)
- View and manage your exercise history

## Contribution
Feel free to fork this repository and submit a pull request.

## License
This project is open-source under the MIT License.

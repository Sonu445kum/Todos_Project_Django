A simple and user-friendly Todo Management System built with Django. This project allows users to create, update, delete, and manage their daily tasks efficiently. It also includes user authentication so that each user can manage their own todos securely.

🚀 Features

🔐 User Authentication (Login, Signup, Logout, Password Reset)

➕ Add Todo – Create new tasks with title and description

✏️ Update Todo – Edit existing tasks easily

🗑️ Delete Todo – Remove tasks you no longer need

✅ Mark as Completed – Track task completion status

👤 User-Specific Todos – Each user can manage their own list

🎨 Attractive UI with Bootstrap 5

🛠️ Tech Stack

Backend: Django, Django ORM

Frontend: HTML, CSS, Bootstrap 5

Database: SQLite (default) / MySQL (can be configured)

Authentication: Django Auth System

📸 Screenshots

Login / Signup Page

Todo List Page

Create / Edit Todo Page

⚙️ Setup Instructions

Clone this repository

git clone https://github.com/your-username/django-todo-app.git
cd django-todo-app


Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Run the server

python manage.py runserver


Open in browser: http://127.0.0.1:8000/


Flow chart of our User Authentications
                        ┌───────────────┐
                        │   Signup      │
                        │(signup view)  │
                        └───────┬───────┘
                                │ Success → redirect to Login
                                │
                                ▼
                        ┌───────────────┐
                        │   Login       │
                        │(login_view)   │
                        └───────┬───────┘
           Wrong credentials  │
           ---------------->  │
           Error message       │
                                ▼
                        ┌───────────────┐
                        │   Home / Todos│
                        │(todos:home)   │
                        └───────┬───────┘
                                │
             ┌──────────────────┴───────────────────┐
             │                                      │
             ▼                                      ▼
     ┌───────────────┐                      ┌───────────────┐
     │  Profile      │                      │ Logout        │
     │(profile view) │                      │(logout_view)  │
     └───────────────┘                      └───────────────┘
             │
             ▼
    ┌─────────────────────┐
    │Change Password       │
    │(change_password)    │
    └─────────────────────┘
             │
             ▼
   ┌─────────────────────────────┐
   │ Password Reset Request      │
   │(password_reset_request)    │
   └─────────────┬──────────────┘
                 │ Email sent with unique link
                 ▼
   ┌─────────────────────────────┐
   │ Password Reset Confirm       │
   │(password_reset_confirm)    │
   └─────────────────────────────┘
                 │
                 ▼
             Set New Password → redirect to Login


flowchart TD
    Signup -->|Success| Login
    Login -->|Valid| Home
    Login -->|Invalid| ErrorMessage
    Home --> Profile
    Home --> Logout
    Profile --> ChangePassword
    ChangePassword --> Home
    Home -->|Forgot Password| PasswordResetRequest
    PasswordResetRequest --> EmailSent
    EmailSent --> PasswordResetConfirm
    PasswordResetConfirm --> Login

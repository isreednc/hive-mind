# Hive Mind
## Overview
A Django-based web application designed to streamline team coordination in the initial stages of school projects. The platform provides intuitive role assignment and task organization through a post-it board interface.

## Features

- Team Role Management: Define and assign project roles with clear responsibilities
- Task Board: Visual task organization with drag-and-drop functionality
- Task Assignment: Assign tasks to specific team members
- Due Date Tracking: Set and monitor task deadlines
- Progress Visualization: Track completion status for individual tasks and overall project
- Comment System: Discuss tasks and share updates within the application

Technology Stack

- Backend: Python 3.x, Django 4.x
- Frontend: HTML, CSS, JavaScript, Bootstrap 5
- Database: SQLite (development), PostgreSQL (production)
- Authentication: Django Authentication System
- Task Board: JavaScript + Django REST Framework

## Installation
### Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

### Setup
```bash
# Clone the repository
git clone https://github.com/yourusername/project-coordination-app.git
cd project-coordination-app

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create admin user
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

## Usage

1. Register a new account or log in
2. Create a new project
3. Invite team members via email
4. Define project roles
5. Create task with progress tag (e.g., "To Do", "In Progress", "Done")
6. Add tasks as digital post-its
7. Assign team members to tasks
8. Drag and drop tasks to organize

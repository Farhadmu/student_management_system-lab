# Student Management System

A simple Student Management System built with **Django** and **SQLite**.
It lets you view, add and edit student records (ID, name, age, department).

## Features

- View all students in a table (home page)
- Add a new student
- Edit an existing student
- Django admin panel for managing data
- *(Delete is not finished yet, see "Known issues")*

## Tech stack

- Python 3.10+
- Django 5.x / 6.x
- SQLite (default, no extra setup)

## Project structure

```
student_management_system-lab/
├── manage.py
├── sms_project/          # project settings and root URLs
│   ├── settings.py
│   └── urls.py
└── sms_app/              # main app
    ├── models.py         # Student model
    ├── views.py          # list, add, edit views
    ├── urls.py           # app routes
    ├── admin.py
    ├── migrations/
    ├── static/css/style.css
    └── templates/
        ├── home.html
        ├── add_student.html
        └── edit_student.html
```

## Setup guide

### 1. Install prerequisites

- [Python](https://www.python.org/downloads/) (tick **"Add Python to PATH"** during install)
- [Git](https://git-scm.com/downloads)

Check both are installed:

```bash
python --version
git --version
```

### 2. Clone the repository

```bash
git clone https://github.com/Farhadmu/student_management_system-lab.git
cd student_management_system-lab
```

### 3. Create and activate a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv senv
senv\Scripts\Activate.ps1
```

If PowerShell blocks the script, run this once and try again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Windows (CMD):**

```cmd
senv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
python3 -m venv senv
source senv/bin/activate
```

You should now see `(senv)` at the start of your terminal prompt.

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

(or simply `pip install django`)

### 5. Set up the database

The database file (`db.sqlite3`) is not stored in the repository, so create it:

```bash
python manage.py migrate
```

### 6. (Optional) Create an admin user

```bash
python manage.py createsuperuser
```

### 7. Run the server

```bash
python manage.py runserver
```

Open in your browser:

| Page | URL |
|------|-----|
| Student list | http://127.0.0.1:8000/ |
| Add student | http://127.0.0.1:8000/add/ |
| Edit student | http://127.0.0.1:8000/edit/<id>/ |
| Admin panel | http://127.0.0.1:8000/admin/ |

Stop the server with `Ctrl + C`.

## Using the app

1. Open the home page and click **Add a new Student**.
2. Fill in ID, Name, Age and Dept, then submit.
3. The student appears in the list. Click **Edit** to change their details.

## Common problems

| Problem | Fix |
|---------|-----|
| `python` is not recognized | Reinstall Python and tick "Add to PATH", then restart the terminal |
| `git` is not recognized | Install Git, then fully close and reopen VS Code |
| `No module named 'django'` | Activate the virtual environment, then `pip install django` |
| `no such table: sms_app_student` | Run `python manage.py migrate` |
| `TemplateDoesNotExist` | Template file name must exactly match the name used in `views.py` |
| Port already in use | Run `python manage.py runserver 8080` |

## Known issues / to do

- `delete_student` view is incomplete and has no URL, so the **Delete** link does nothing yet.
- The "No Student Found!" row uses `colspan="4"` but the table has 5 columns.
- The edit form button says "Add" instead of "Update".

## Git workflow

```bash
git add .
git commit -m "Describe your change"
git push
```

## License

For educational use (software lab project).

This project collects data from New Relic via API, customizes it, stores it in a local database then presents it in the webapp

My application is a Dockerized web application built with Django.

---

## Tech Stack
- Python 3.12
- Django 4.x
- PostgreSQL
- Docker
- Docker Compose

---

## Project Structure

.
├── docker-compose.yml
├── Dockerfile
├── Dockerfile_basic
├── manage.py
├── myproject
│   ├── asgi.py
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-314.pyc
│   │   ├── settings.cpython-314.pyc
│   │   ├── urls.cpython-314.pyc
│   │   ├── views.cpython-314.pyc
│   │   └── wsgi.cpython-314.pyc
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── README.txt
├── requirements.txt
├── sla_report
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── management
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   ├── __pycache__
│   │   │   └── slareport.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       └── __init__.cpython-314.pyc
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-314.pyc
│   │       └── __init__.cpython-314.pyc
│   ├── models.py
│   ├── __pycache__
│   │   ├── admin.cpython-314.pyc
│   │   ├── apps.cpython-314.pyc
│   │   ├── __init__.cpython-314.pyc
│   │   ├── models.cpython-314.pyc
│   │   ├── urls.cpython-314.pyc
│   │   └── views.cpython-314.pyc
│   ├── sla_report.csv
│   ├── templatetags
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-314.pyc
│   │   │   └── sla_report_extras.cpython-314.pyc
│   │   └── sla_report_extras.py
│   ├── tests.py
│   ├── urls.py
│   ├── urls.py_origin
│   ├── views.py
│   └── views.py_origin
├── start.sh
├── templates
│   ├── base.html
│   ├── errors
│   │   └── 404.html
│   ├── footer.html
│   ├── header.html
│   ├── home.html
│   ├── registration
│   │   └── login.html
│   └── sla_report
│       ├── add_data2html.sh
│       ├── non_prefix_group_or_single.html
│       ├── prefix_group_or_single.html
│       ├── setCellColor.html
│       ├── setGrpCellColor.html
│       └── summary.html
└── webstatic
    ├── css
    │   ├── collapsible.css
    │   ├── navigation.css
    │   └── tables.css
    └── js
        └── sla_report.js

19 directories, 62 files

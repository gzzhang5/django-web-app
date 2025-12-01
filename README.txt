The project directory tree:

tree -L 4
.
├── docker-compose.yml
├── Dockerfile
├── Dockerfile_basic
├── helloworld
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
├── myproject
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── requirements.txt
├── sla_report
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── management
│   │   ├── commands
│   │   │   ├── __init__.py
│   │   │   └── slareport.py
│   │   └── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── README.txt
│   ├── sla_report.csv
│   ├── templatetags
│   │   ├── __init__.py
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
        └── sre_reports.js

16 directories, 54 files


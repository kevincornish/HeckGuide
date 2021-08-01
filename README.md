# HeckGuide

Install Python

Create and enter new working directory eg "HeckGuide"

Create Virtual Environment 

Mac/Unix
```
py -m venv env
source env/bin/activate
```
Windows
```
.\env\Scripts\activate
```

Install requirements for local development
```
pip install -r requirements/base.txt
pip install -r requirements/local.txt
```

Install postgres

Create a new database

Fill in ```heckguide/sample.env``` and rename to ```.env```

Make migrations and then run migrations
```
python manage.py makemigrations
python manage.py migrate
```

Create a superuser
```
python manage.py createsuperuser
```

Run server
```
python manage.py runserver
```

Open website
```
http://127.0.0.1:8000/
```
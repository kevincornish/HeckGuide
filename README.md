# HeckGuide

Install Python

Install Postgres

Create and enter new working directory eg "HeckGuide"

Create Virtual Environment 
```
py -m venv env
```
Activate Environment
Mac/Unix
```
source env/bin/activate
```
Windows
```
.\env\Scripts\activate
```

Install requirements for local development
```
pip install -r requirements/local.txt
```

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

Generate an API token for the newly created superuser
```
python manage.py drf_create_token superusername
```

Run server
```
python manage.py runserver
```

Open website
```
http://127.0.0.1:8000/
```
Development website
```
https://v2.heckguide.com/
```
## Commands 
Scrapes a set number of allies '5000' already in the database without fully populated info and fills them, then scrapes the owner and that owner etc. Depth set to '3'
```
python manage.py crawl_allies_by_name 5000 3
```
Scrapes allys by price '500000' and set number of pages '1', a random token will be picked to scrape.
```
python manage.py find_allies_by_price 500000 1
```
Scrapes allys by random price and random number of pages
```
python manage.py find_random_price_allies
```
Purchase an ally via supplied username with token
```
python manage.py buy_ally_by_name kevz 23
```
Volley an ally between tokens
```
python manage.py volley kevz
```
Strip a users allies, token must be given
```
python manage.py strip_allies kevz 23
```
Scrape the realm starting at the lower boundry of the map, loading 20 chunks and stepping through to the upper end, pick which realm to crawl passing the token argument
```
python manage.py crawl_world 1
```
Scrape the realms chat history
```
python manage.py poll_map 1
```
# Instructions

### Heroku

Install the Heroku CLI
```
$ sudo snap install --classic heroku
```

Start app locally
```
$ heroku local -p 8000
```

### Django

Create virtual environment
```
$ python3 -m venv venv
```

Activate virtual environment
```
$ source venv/bin/activate
```

Install dependencies
```
$ python3 -m pip install -r requirements.txt
```

Initialize database
```
$ python3 manage.py migrate
```

Start backend
```
$ python3 manage.py runserver --noreload
```

### PostgreSQL

Install PostgreSQL
```
$ sudo apt-get install -y postgresql postgresql-contrib
```

Set up new user
```
$ sudo -u postgres psql -f postgres.sql
```

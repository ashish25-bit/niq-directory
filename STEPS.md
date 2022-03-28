* Install django
```cmd
pip install django --user
```

* create a django project
```cmd
django-admin startproject mysite .
```

* start the django server
```python
python manage.py runserver
```

* migrate the django project
```cmd
python manage.py migrate
```

* create an app in django <br/> after creating an app make a **urls.py** in __APP_NAME/urls.py__
```cmd
python manage.py startapp <APP_NAME>
```

* create a super user in django
```cmd
python manage.py createsuperuser
```

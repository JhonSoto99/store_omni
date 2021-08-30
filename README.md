# store-omni(Python 3.9)

######(you must have rabbitmq installed previously)


### Running server celery and rabbitmq(Send notifications async)

* `brew services start rabbitmq`
* `celery -A store_omni worker --loglevel=info`

### Running server Django project
##### The virtual environment must be previously created and activated with python3.9

* `pip install -r requirements.txt`
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py runserver`

### Hostnames for accessing the service directly

* Local: http://127.0.0.1:8000


### Django RestFramework

* Url documentation Api: https://documenter.getpostman.com/view/7639691/TzzHnDCV


### The sql that should be used to generate the report of the orders sent and delivered is:

* `SELECT * FROM  orders_order WHERE paid_out=1 AND sent=1;`
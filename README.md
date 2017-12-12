# Private Message App

This is a user to user private messaging app developed with Django, with the help of django-postman, django-user-accounts and some other packages included in requirements.txt

To run this app you need to create a virtual environment and install requirements using pip as follows:

[Install Redis in your system](https://redis.io/download)

>cd "Your Project Directory"

>virtualenv venv

>source venv/bin/activate

>pip install -U pip

>pip install -r requirements.txt 

>python3 manage.py migrate

>python3 manage.py runserver


Make sure to modify MEDIA_ROOT path in settings.py:

MEDIA_ROOT = '/YOUR PROJECT DIRECTORY/private_message_app/media'

# Effector database
#### Version 0.1.0
Effector database is a Django app that contains information about effectors.
Visitors can view, search and edit effectors in the database.
There is also the option to add new effectors to the database.

## Quick start
### Requirements
- Python 3 (verrified for v3.7 and v3.8)
- Django 3 (verrified for v3.1)
- [Basic knowledge about Django](https://docs.djangoproject.com/en/3.1/intro/)

### Installation
1. Install this github repository:
`git clone https://github.com/LuukHenk/effector_database.git`

2. Copy the `effector_database` folder in the repository to your django project folder (same directory as the `manage.py` file):
`cp -r effector_database/effector_database dir/to/your/project/`
3. Add "effector_database" to your projects INSTALLED_APPS setting like this:
	```
    INSTALLED_APPS = [
        ...
        'effector_database',
    ]
	```
4. Include the effector_database URLconf in your project urls.py like this (Make sure you also import the "include" function from django.urls):
	`path('effector_database/', include('effector_database.urls')),`

5. Run `python manage.py makemigrations effector_database && python manage.py migrate` to create the effector_database models.

6. Run the server: `python manage.py runserver` and visit http://127.0.0.1:8000/effector_database/ to view the database.

7. Additional changes can be made to the database as admin via
   http://127.0.0.1:8000/admin/ (you'll need the Admin app enabled)

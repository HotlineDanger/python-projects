### python manage.py runserver
''' Run the django python server '''

### python manage.py makemigrations learning_logs
 '''The command makemigrations tells Django to figure out how to modify
the database so it can store the data associated with any new models we’ve
defined. The output here shows that Django has created a migration file
called 0001_initial.py. This migration will create a table for the model Topic
in the database. Now we’ll apply this migration and have Django modify the database
for us:'''
### python mananage.py migrate
''' Whenever we want to modify the data that Learning Log manages,
we’ll follow these three steps: modify models.py, call makemigrations on
learning_logs, and tell Django to migrate the project '''


### (winpty could be needed on winbouse) python manage.py createsuperuser
'''To create a superuser in Django, enter the following command'''


### http://localhost:8000/admin/ to access the admin page
''' Now use the superuser account to access the admin site. Go to http://localhost:8000/admin/ '''
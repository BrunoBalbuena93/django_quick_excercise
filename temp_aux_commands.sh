# Some debugging commands I like to keep close when developing

python manage.py showmigrations
python manage.py showmigrations --database "project_admin_auth_users_db"
python manage.py showmigrations --database "users_pets_api"

python manage.py makemigrations
python manage.py makemigrations users_pets_api

python manage.py migrate
python manage.py migrate --database "project_admin_auth_users_db"
python manage.py migrate --database "users_pets_api"

python manage.py createsuperuser --database "users_pets_api"

python manage.py shell

  from users_pets_api.models import Person, Pet, Owner
  Pet.objects.filter (id = 1).get ().owners.all ()
  Person.objects.filter (id = 2).get ().pets.all ()

python manage.py runserver localhost:42800

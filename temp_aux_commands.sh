# Some debugging commands I like to keep close when developing

python manage.py showmigrations

python manage.py makemigrations
python manage.py migrate --database "project_admin_auth_users_db"
python manage.py migrate --database "users_pets_api"

python manage.py runserver localhost:42800

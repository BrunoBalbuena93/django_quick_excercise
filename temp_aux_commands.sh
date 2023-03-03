# Some debugging commands I like to keep close when developing

python manage.py showmigrations
python manage.py showmigrations --database "project_admin_auth_users_db"
python manage.py showmigrations --database "users_pets_api"

python manage.py makemigrations
python manage.py makemigrations users_pets_api

python manage.py migrate
python manage.py migrate --database "project_admin_auth_users_db"
python manage.py migrate --database "users_pets_api"

python manage.py loaddata users_pets_api/fixtures/person_initial_data.json --database "users_pets_api"
python manage.py loaddata users_pets_api/fixtures/pet_initial_data.json --database "users_pets_api"
python manage.py loaddata users_pets_api/fixtures/owner_initial_data.json --database "users_pets_api"
python manage.py loaddata users_pets_api/fixtures/permission_initial_data.json --database "users_pets_api"

python manage.py createsuperuser --database "users_pets_api"

python manage.py shell

  from users_pets_api.models import Person, Pet, Owner
  Pet.pets.filter (id = 1).get ().owners.all ()
  Pet.pets.filter (id = 10).get ().owners.all ()
  Person.people.filter (id = 1).get ().pets.all ()
  Person.people.filter (id = 10).get ().pets.all ()

python manage.py runserver localhost:42800

# All permission (with all)
curl -X POST -H "Content-Type: application/json" -d '{"username": "leafpetrichorwebrye", "password": "password"}' http://localhost:42800/api-v0-jwt/token/

# All permission (without sensitive)
curl -X POST -H "Content-Type: application/json" -d '{"username": "volleyballanniehall", "password": "password"}' http://localhost:42800/api-v0-jwt/token/

# Read permission (with all)
# Delete permission (without sensitive)
curl -X POST -H "Content-Type: application/json" -d '{"username": "orangejuicedrumpig", "password": "password"}' http://localhost:42800/api-v0-jwt/token/

# Create permission (with all)
curl -X POST -H "Content-Type: application/json" -d '{"username": "crocodilefloraseaice", "password": "password"}' http://localhost:42800/api-v0-jwt/token/

# Update permission (with all)
curl -X POST -H "Content-Type: application/json" -d '{"username": "moderntimesicecream", "password": "password"}' http://localhost:42800/api-v0-jwt/token/

# Delete permission (with all)
curl -X POST -H "Content-Type: application/json" -d '{"username": "winevenuspeacefullog", "password": "password"}' http://localhost:42800/api-v0-jwt/token/

# Read permission (without sensitive)
curl -X POST -H "Content-Type: application/json" -d '{"username": "beetmarramgloveegg", "password": "password"}' http://localhost:42800/api-v0-jwt/token/

# Create permission (without sensitive)
curl -X POST -H "Content-Type: application/json" -d '{"username": "icehamstersnowstorm", "password": "password"}' http://localhost:42800/api-v0-jwt/token/

# Update permission (without sensitive)
curl -X POST -H "Content-Type: application/json" -d '{"username": "leiatennisstardust", "password": "password"}' http://localhost:42800/api-v0-jwt/token/

# No permission
curl -X POST -H "Content-Type: application/json" -d '{"username": "pigeongrapecamelnet", "password": "password"}' http://localhost:42800/api-v0-jwt/token/


curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/owner/
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/owner/
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/owner/
curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/owner/
curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/owner/

curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/person/
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/person/
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/person/
curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/person/
curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/person/

curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/pet/
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/pet/
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/pet/
curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/pet/
curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/pet/


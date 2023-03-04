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

# DOT Application permissions
curl -X POST  -d 'grant_type=password' -d 'client_id=Ba0HFa3jm4u4R6PKVFUKjqnE9QkR2vMmGIj89hIB' -d 'client_secret=HVSFufYLHd775mdiANZ5KwRK2PFwEhNHMWsa4QZ57kPLLiGcTPVyQflnS9vvoaY44GD6AE3o7tnIknL8VfUtbq5ZvFbi2WRjzaqlxOs7taXVCtVS4jnfNJCkkDutjNr9' -d 'username=pigeongrapecamelnet' -d 'password=password' -d 'scope=read-all' http://localhost:42800/api-v0-dot/token/
curl -X POST  -d 'grant_type=password' -d 'client_id=Ba0HFa3jm4u4R6PKVFUKjqnE9QkR2vMmGIj89hIB' -d 'client_secret=HVSFufYLHd775mdiANZ5KwRK2PFwEhNHMWsa4QZ57kPLLiGcTPVyQflnS9vvoaY44GD6AE3o7tnIknL8VfUtbq5ZvFbi2WRjzaqlxOs7taXVCtVS4jnfNJCkkDutjNr9' -d 'username=pigeongrapecamelnet' -d 'password=password' -d 'scope=create-all' http://localhost:42800/api-v0-dot/token/
curl -X POST  -d 'grant_type=password' -d 'client_id=Ba0HFa3jm4u4R6PKVFUKjqnE9QkR2vMmGIj89hIB' -d 'client_secret=HVSFufYLHd775mdiANZ5KwRK2PFwEhNHMWsa4QZ57kPLLiGcTPVyQflnS9vvoaY44GD6AE3o7tnIknL8VfUtbq5ZvFbi2WRjzaqlxOs7taXVCtVS4jnfNJCkkDutjNr9' -d 'username=pigeongrapecamelnet' -d 'password=password' -d 'scope=read-not-sensitive' http://localhost:42800/api-v0-dot/token/

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

curl -X POST -F date_of_birth="2023-03-02 02:10:00Z" -F chip_number="1111" -F gender="F" -F weight=47.89 -F breed="Pomeranian" -F pet_image=@"/home/jctrujillo/Downloads/dog-1.jpg" http://localhost:42800/api-v0/pet/
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/pet/
curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/pet/

curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/hyperlinked-person/
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/hyperlinked-person/
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/hyperlinked-person/
curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/hyperlinked-person/
curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/hyperlinked-person/


curl -X POST  http://localhost:42800/api-v0/hyperlinked-person/ -F id=5 -F username="forrestgumpsavannah" -F first_name="Savannah 1" -F last_name="Harrison 2" -F email="forrestgumpsavannah@yahoo.com" -F date_joined="2023-02-01T00:00:00Z" -F phone_number="+573333014786" -F city="Cali" -F person_image=@"/home/jctrujillo/Downloads/dog-1.jpg"

curl -X GET -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/hyperlinked-pet/
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/hyperlinked-pet/
curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/hyperlinked-pet/
curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/hyperlinked-pet/
curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer " http://localhost:42800/api-v0/hyperlinked-pet/



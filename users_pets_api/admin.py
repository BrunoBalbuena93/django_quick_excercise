from django.contrib import admin

# Register your models here.
from users_pets_api.admins import (
    OwnerAdmin,
    PersonAdmin,
    PetAdmin
)

from users_pets_api.models import (
    Owner,
    Person,
    Pet
)

admin.site.register (Owner, OwnerAdmin)
admin.site.register (Person, PersonAdmin)
admin.site.register (Pet, PetAdmin)

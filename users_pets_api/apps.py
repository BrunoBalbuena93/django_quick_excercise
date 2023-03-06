from django.apps import AppConfig
from django.db.models.signals import post_delete, post_save

from users_pets_api.signals import (
    delete_old_person_images,
    delete_old_pet_images,
    delete_pet_images_path,
    delete_person_images_path
)


class UserPetsApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_pets_api'

    def ready(self):
        person_model = self.get_model('Person')
        post_delete.connect(delete_person_images_path, sender=person_model)
        post_save.connect(delete_old_person_images, sender=person_model)

        pet_model = self.get_model('Pet')
        post_delete.connect(delete_pet_images_path, sender=pet_model)
        post_save.connect(delete_old_pet_images, sender=pet_model)

from django.db import models as models

from users_pets_api.querysets import OwnerQuerySet


class OwnerManager (models.Manager):

    def get_query_set (self):

        return OwnerQuerySet (self.model, using = self._db)

    def get_all (self):

        return self.get_query_set ().get_all ()

    def get_by_person_id (self, id):

        return self.get_query_set ().get_by_person_id (id)

    def get_by_pet_id (self, id):

        return self.get_query_set ().get_by_pet_id (id)

    def get_by_person_id_and_pet_id (self, person_id, pet_id):

        return self.get_by_person_id (person_id).get_by_pet_id (pet_id)

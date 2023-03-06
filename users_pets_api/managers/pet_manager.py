from django.db import models as models

from users_pets_api.querysets import PetQuerySet


class PetManager (models.Manager):

    def get_query_set (self):

        return PetQuerySet (self.model, using = self._db)

    def get_all (self):

        return self.get_query_set ().get_all ()

    def get_by_id (self, id):

        return self.get_query_set ().get_by_id (id)

    def get_by_person_id (self, id):

        return self.get_query_set ().get_by_person_id (id)

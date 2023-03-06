from django.db import models as models

from users_pets_api.querysets import PersonQuerySet


class PersonManager (models.Manager):

    def get_query_set (self):

        return PersonQuerySet (self.model, using = self._db)

    def get_all (self):

        return self.get_query_set ().get_all ()

    def get_by_id (self, id):

        return self.get_query_set ().get_by_id (id)

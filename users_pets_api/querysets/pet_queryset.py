from django.db import models as models


class PetQuerySet (models.query.QuerySet):

    def get_all (self):

        return self.all()

    def get_by_id (self, id):

        return self.filter(id=id)

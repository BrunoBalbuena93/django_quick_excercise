from django.db import models as models


class OwnerQuerySet (models.query.QuerySet):

    def get_all (self):

        return self.all()

    def get_by_person_id (self, id):

        return self.filter(person_id=id)

    def get_by_pet_id (self, id):

        return self.filter(pet_id=id)

    def get_by_person_id_and_pet_id (self, person_id, pet_id):

        return self.filter(pet_id=pet_id, person_id=person_id)

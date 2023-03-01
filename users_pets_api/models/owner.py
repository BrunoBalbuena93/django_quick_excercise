from django.db import models as models

from .person import Person
from .pet import Pet


class Owner(models.Model):

    person = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        db_column='person_id',
        to_field='id',
        blank=False,
        null=False
    )
    pet = models.ForeignKey(
        Pet,
        on_delete=models.CASCADE,
        db_column='pet_id',
        to_field='id',
        blank=False,
        null=False
    )

    class Meta:
        app_label = 'users_pets_api'
        db_table = 'owner'
        ordering = ['person', 'pet']
        constraints = [
            models.UniqueConstraint(
                fields=('person', 'pet'),
                name='unique_person_id_pet_id'
            )
        ]

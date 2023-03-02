from django.db import models as models
from django.contrib.auth.models import AbstractUser, UserManager

from phonenumber_field.modelfields import PhoneNumberField

from users_pets_api.managers import PersonManager

# Notes:
#  - city could also be a model or table if more customization and associated data is needed, with a "one-to-many
#    relationship" or a "many-to-many relationships" between city and person (a city is the living place of many
#    people, a person lives only in one city, a person can live in many cities ... etc). For simplicity it is not
#    implemented in this exercise
#  - Phone number information could also be a model or table if more customization and associated data is needed, with
#    a "one-to-many relationship" or a "many-to-many relationships" between the contact and person (a person can be
#    contacted by multiple phone numbers, a phone number can only contact one person, a phone number can contact many
#    persons ... etc). For simplicity it is not implemented in this exercise (but assumed as unique)
#  - Char fields data lengths are assumed but ideally must be validated with some domain data samples


class Person(AbstractUser):

    phone_number = PhoneNumberField(
        db_column='phone_number',
        blank=False,
        null=False,
        unique=True
    )
    city = models.CharField(
        db_column='city',
        max_length=75,
        blank=False,
        null=False,
        unique=False
    )

    objects = UserManager()
    people = PersonManager()

    class Meta:
        app_label = 'users_pets_api'
        db_table = 'person'
        ordering = ['phone_number', 'city', 'last_login']

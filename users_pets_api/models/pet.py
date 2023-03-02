from django.db import models as models
from django.core.validators import MinValueValidator
from django.utils import timezone

from users_pets_api.managers import PetManager

from .person import Person

# Notes:
#  - gender and breed could also be models or tables if more customization and associated data is needed, with "one-to-
#    many relationships" between them and the pet model (a pet has only one gender and a breed, there are many pets
#    from a single breed, there are many pets from a single gender, ... etc). For simplicity it is not implemented in
#    this exercise
#  - Added an id field to the pet (since i didn't really know which combination of table fields were unique and I
#    always prefer a unique constraint for every model or table)
#  - Char fields data lengths are assumed but ideally must be validated with some domain data samples


class Pet(models.Model):

    id = models.AutoField(
        db_column='id',
        blank=False,
        null=False,
        unique=True,
        editable=False,
        primary_key=True
    )
    date_of_birth = models.DateTimeField(
        db_column='date_of_birth',
        blank=False,
        null=False,
        unique=False
    )
    gender = models.CharField(
        db_column='gender',
        max_length=1,
        blank=False,
        null=False,
        unique=False,
        choices=(
            ("F", "Female"),
            ("M", "Male")
        )
    )
    weight = models.FloatField(
        db_column='weight',
        blank=False,
        null=False,
        unique=False,
        validators=[
            MinValueValidator(0.0)
        ]
    )
    breed = models.CharField(
        db_column='breed',
        max_length=50,
        blank=False,
        null=False,
        unique=False
    )
    deceased_date = models.DateTimeField(
        db_column='deceased_date',
        blank=True,
        null=True,
        unique=False
    )
    owners = models.ManyToManyField(
        Person,
        related_name='pets',
        through='Owner'
    )

    pets = PetManager()

    def calculate_age(self):
        date_to_calculate_age = timezone.now()

        if not(self.deceased_date is None):
            date_to_calculate_age = self.deceased_date

        return date_to_calculate_age - self.date_of_birth

    @property
    def age_seconds(self):
        return self.calculate_age().total_seconds()

    @property
    def age_minutes(self):
        return self.age_seconds / 60.0

    @property
    def age_hours(self):
        return self.age_minutes / 60.0

    @property
    def age_days(self):
        return self.age_hours / 24.0

    @property
    def age_years(self):
        return self.age_days / 365.25

    class Meta:
        app_label = 'users_pets_api'
        db_table = 'pet'
        ordering = ['date_of_birth', 'deceased_date', 'breed', 'gender', 'weight', 'id']
        constraints = [
            models.CheckConstraint(
                check=(models.Q(deceased_date__isnull = True)) |
                      (models.Q(deceased_date__gt = models.F('date_of_birth'))),
                name='deceased_date_gt_date_of_birth'
            )
        ]

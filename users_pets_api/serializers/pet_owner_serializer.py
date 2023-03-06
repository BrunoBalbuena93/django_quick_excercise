from rest_framework import serializers as serializers

from users_pets_api.models import Pet


class PetOwnerSerializer(serializers.ModelSerializer):

    age = serializers.SerializerMethodField('get_age')

    def get_age(self, instance):
        return {
            "seconds": instance.age_seconds,
            "minutes": instance.age_minutes,
            "hours": instance.age_hours,
            "days": instance.age_days,
            "years": instance.age_years
        }

    class Meta:

        model = Pet

        fields = [
            'id',
            'chip_number',
            'date_of_birth',
            'gender',
            'weight',
            'breed',
            'deceased_date',
            'age',
            'pet_image'
        ]

        # Note:
        #   - This is an example of read only fields. Depending on the use case they can be writable fields. I just
        #     wanted to show an example of read_only_fields here
        read_only_fields = [
            'id',
            'age'
        ]

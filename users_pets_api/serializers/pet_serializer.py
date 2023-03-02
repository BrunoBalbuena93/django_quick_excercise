from rest_framework import serializers as serializers

from users_pets_api.models import Pet


class PetSerializer(serializers.ModelSerializer):

    class Meta:

        model = Pet

        fields = [
            'id',
            'date_of_birth',
            'gender',
            'weight',
            'breed',
            'deceased_date'
        ]

        # Note:
        #   - This is an example of read only fields. Depending on the use case they can be writable fields. I just
        #     wanted to show an example of read_only_fields here
        read_only_fields = [
            'id'
        ]

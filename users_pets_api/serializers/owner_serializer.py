from rest_framework import serializers as serializers

from users_pets_api.models import Owner

from .person_serializer import PersonSerializer
from .pet_serializer import PetSerializer


class OwnerSerializer(serializers.ModelSerializer):

    person = PersonSerializer(read_only=False, many=False)
    pet = PetSerializer(read_only=False, many=False)

    class Meta:

        model = Owner

        fields = [
            'id',
            'person',
            'pet'
        ]

        # Note:
        #   - This is an example of read only fields. Depending on the use case they can be writable fields. I just
        #     wanted to show an example of read_only_fields here
        read_only_fields = [
            'id',
            'owner',
            'pet'
        ]

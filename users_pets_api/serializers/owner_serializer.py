from rest_framework import serializers as serializers
from rest_framework.validators import UniqueTogetherValidator

from users_pets_api.models import Owner
from users_pets_api.models import Person
from users_pets_api.models import Pet

from .person_serializer import PersonSerializer
from .pet_serializer import PetSerializer


class OwnerSerializer(serializers.ModelSerializer):

    person = PersonSerializer(read_only=True, many=False)
    pet = PetSerializer(read_only=True, many=False)

    person_id = serializers.PrimaryKeyRelatedField(
        queryset=Person.people.get_all(), many=False, read_only=False, source='person', write_only=True
    )
    pet_id = serializers.PrimaryKeyRelatedField(
        queryset=Pet.pets.get_all(), many=False, read_only=False, source='pet', write_only=True
    )

    class Meta:

        model = Owner

        fields = [
            'id',
            'person',
            'person_id',
            'pet',
            'pet_id'
        ]

        read_only_fields = [
            'id',
            'person',
            'pet'
        ]

        extra_kwargs = {
            'person_id': {'write_only': True},
            'pet_id': {'write_only': True}
        }

        validators = [
            UniqueTogetherValidator(
                queryset=Owner.owners.all(),
                fields=['person_id', 'pet_id']
            )
        ]

from rest_framework import serializers as serializers

from users_pets_api.models import Pet


class HyperlinkedPetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:

        model = Pet

        fields = [
            'id',
            'date_of_birth',
            'gender',
            'weight',
            'breed',
            'deceased_date',
            'owners'
        ]

        # Note:
        #   - This is an example of read only fields. Depending on the use case they can be writable fields. I just
        #     wanted to show an example of read_only_fields here
        read_only_fields = [
            'id'
        ]

        extra_kwargs = {
            'owners': {
                'view_name': 'users_pets_api:person-resource-by-id-with-slash',
                'lookup_field': 'id'
            }
        }

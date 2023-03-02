from rest_framework import serializers as serializers

from users_pets_api.models import Person


class PersonSerializer(serializers.ModelSerializer):

    class Meta:

        model = Person

        # Note:
        #  - The password, is_superuser, is_staff, is_active fields are is a sensitive data fields, so they are not
        #    shown or accepted for the serializer. In case there is a functionality needed to manipulate information
        #    from these fields there are better login related options from the framework which are more secure than
        #    the API endpoint that would be exposed with this serializer (Even some parameters I include for this
        #    exercise may be deemed as insecure to show, such as the id, username, first and last names ... and could
        #    be needed to be deleted in order to avoid security attacks)
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'date_joined',
            'phone_number',
            'city',
            'last_login'
        ]

        # Note:
        #   - This is an example of read only fields. Depending on the use case they can be writable fields. I just
        #     wanted to show an example of read_only_fields here
        read_only_fields = [
            'id',
            'username',
            'date_joined'
        ]

        # Note:
        #  - This is an example of some write only fields. Depending on the use case they can be readable fields. I
        #    just
        extra_kwargs = {
            'email': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True}
        }

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from django_app.permissions import DjangoAppBaseResourcePermission

from users_pets_api.models import Pet

from users_pets_api.serializers import PetOwnerSerializer


class PetOwnerAPIView(APIView):

    # Note:
    #   - I could have used a setting from django rest framework to set up the authentication classes and permissions
    #     directly, but I used the authentication_classes, permission_classes, required_scopes and permission map
    #     fields to show an exercise using a simple JWT approach and a simple Token OAuth2 authentication (and how
    #     they can be used together from the implementation). In a real world example only one authentication and
    #     authorization method should be used (and might need to be configured in a more detailed way, for instance
    #     with a configuration based on cryptography keys and introspection endpoints, to try to avoid security issues).

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, DjangoAppBaseResourcePermission]
    app_label = 'users_pets_api'
    resource_name = 'owner'

    @method_decorator(csrf_exempt)
    def get (self, request, person_id = None, *args, **kwargs):

        pet_owner_data = Pet.pets.get_all()

        if not(person_id is None):
            pet_owner_data = pet_owner_data.get_by_person_id(person_id)

        if pet_owner_data.exists():

            pet_owner_serialized_data = PetOwnerSerializer(
                pet_owner_data,
                many=True,
                context={"request": request}
            )
            return Response(pet_owner_serialized_data.data)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

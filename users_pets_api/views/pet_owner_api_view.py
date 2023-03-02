from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# from oauth2_provider.contrib.rest_framework import OAuth2Authentication
# from oauth2_provider.contrib.rest_framework import TokenHasScope

from users_pets_api.models import Pet

from users_pets_api.serializers import PetOwnerSerializer


class PetOwnerAPIView(APIView):

#    authentication_classes = [OAuth2Authentication]
#    permission_classes     = [TokenHasScope]
#    required_scopes        = ['']

    @method_decorator(csrf_exempt)
    def get (self, request, person_id = None, *args, **kwargs):

        pet_owner_data = Pet.pets.get_all()

        if not(person_id is None):
            pet_owner_data = pet_owner_data.get_by_person_id(person_id)

        pet_owner_serialized_data = PetOwnerSerializer(
            pet_owner_data,
            many=True,
            context={"request": request}
        )
        return Response(pet_owner_serialized_data.data)

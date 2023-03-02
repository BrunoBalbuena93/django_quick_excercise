from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# from oauth2_provider.contrib.rest_framework import OAuth2Authentication
# from oauth2_provider.contrib.rest_framework import TokenHasScope

from users_pets_api.models import Owner

from users_pets_api.serializers import OwnerSerializer


class OwnerAPIView(APIView):

#    authentication_classes = [OAuth2Authentication]
#    permission_classes     = [TokenHasScope]
#    required_scopes        = ['']

    @method_decorator(csrf_exempt)
    def get (self, request, person_id = None, pet_id = None, *args, **kwargs):

        owner_data = Owner.owners.get_all()

        if not(person_id is None):
            owner_data = owner_data.get_by_person_id(person_id)

        if not(pet_id is None):
            owner_data = owner_data.get_by_pet_id(pet_id)

        owner_serialized_data = OwnerSerializer(
            owner_data,
            many=True,
            context={"request": request}
        )
        return Response(owner_serialized_data.data)

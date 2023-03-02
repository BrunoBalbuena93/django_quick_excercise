from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# from oauth2_provider.contrib.rest_framework import OAuth2Authentication
# from oauth2_provider.contrib.rest_framework import TokenHasScope

from users_pets_api.models import Pet

from users_pets_api.serializers import HyperlinkedPetSerializer


class HyperlinkedPetAPIView (APIView):

#    authentication_classes = [OAuth2Authentication]
#    permission_classes     = [TokenHasScope]
#    required_scopes        = ['']

    @method_decorator(csrf_exempt)
    def get (self, request, id = None, *args, **kwargs):

        if id is None:
            pet_data = Pet.pets.get_all()
            pet_serialized_data = HyperlinkedPetSerializer(
                pet_data,
                many=True,
                context={"request": request}
            )
            return Response(pet_serialized_data.data)

        pet_data = Pet.pets.get_by_id(id)

        if pet_data.exists():

            pet_serialized_data = HyperlinkedPetSerializer(
                pet_data.get(),
                many=False,
                context={"request": request}
            )
            return Response(pet_serialized_data.data)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

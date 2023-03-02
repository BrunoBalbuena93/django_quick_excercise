from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# from oauth2_provider.contrib.rest_framework import OAuth2Authentication
# from oauth2_provider.contrib.rest_framework import TokenHasScope

from users_pets_api.models import Pet

from users_pets_api.serializers import PetSerializer


class PetAPIView (APIView):

#    authentication_classes = [OAuth2Authentication]
#    permission_classes     = [TokenHasScope]
#    required_scopes        = ['']

    @method_decorator(csrf_exempt)
    def get(self, request, id = None, *args, **kwargs):

        if id is None:
            pet_data = Pet.pets.get_all()
            pet_serialized_data = PetSerializer(
                pet_data,
                many=True,
                context={"request": request}
            )
            return Response(pet_serialized_data.data)

        pet_data = Pet.pets.get_by_id(id)

        if pet_data.exists():

            pet_serialized_data = PetSerializer(
                pet_data.get(),
                many=False,
                context={"request": request}
            )
            return Response(pet_serialized_data.data)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):

        pet_request_data = request.data

        pet_serialized_data = PetSerializer(
            data=pet_request_data,
            context={"request" : request}
        )

        if pet_serialized_data.is_valid ():

            pet_serialized_data.save()
            return Response (
                pet_serialized_data.data,
                status=status.HTTP_201_CREATED
            )

        return Response (
            pet_serialized_data.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    @method_decorator(csrf_exempt)
    def put(self, request, id = None, *args, **kwargs):

        pet_request_data = request.data

        if not(id is None):

            pet_data = Pet.pets.get_by_id(id)

            if pet_data.exists():

                pet_serialized_data = PetSerializer(
                    pet_data.get(),
                    data=pet_request_data,
                    context={"request" : request}
                )

                if pet_serialized_data.is_valid ():

                    pet_serialized_data.save()
                    return Response (pet_serialized_data.data)

                return Response(
                    pet_serialized_data.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response (
            'An update request must include the id parameter as part of the URL',
            status = status.HTTP_400_BAD_REQUEST
        )

    @method_decorator(csrf_exempt)
    def patch(self, request, id = None, *args, **kwargs):

        pet_request_data = request.data

        if not(id is None):

            pet_data = Pet.pets.get_by_id(id)

            if pet_data.exists():

                pet_serialized_data = PetSerializer(
                    pet_data.get(),
                    data=pet_request_data,
                    context={"request" : request}
                )

                if pet_serialized_data.is_valid ():

                    pet_serialized_data.save()
                    return Response (pet_serialized_data.data)

                return Response(
                    pet_serialized_data.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response (
            'An update request must include the id parameter as part of the URL',
            status = status.HTTP_400_BAD_REQUEST
        )

    @method_decorator(csrf_exempt)
    def delete(self, request, id = None, *args, **kwargs):

        if not(id is None):

            pet_data = Pet.pets.get_by_id(id)

            if pet_data.exists():
                pet_data.delete()
                return Response (status=status.HTTP_204_NO_CONTENT)

            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        return Response (
            'A delete request must include the id parameter as part of the URL',
            status = status.HTTP_400_BAD_REQUEST
        )

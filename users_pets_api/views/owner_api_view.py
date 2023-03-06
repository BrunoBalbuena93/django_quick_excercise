from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from django_app.permissions import DjangoAppBaseResourcePermission

from users_pets_api.models import Owner

from users_pets_api.serializers import OwnerSerializer


class OwnerAPIView(APIView):

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
    def get(self, request, person_id = None, pet_id = None, *args, **kwargs):

        owner_data = Owner.owners.get_all()

        if not(person_id is None):
            owner_data = owner_data.get_by_person_id(person_id)

        if not(pet_id is None):
            owner_data = owner_data.get_by_pet_id(pet_id)

        if owner_data.exists():

            owner_serialized_data = OwnerSerializer(
                owner_data,
                many=True,
                context={"request": request}
            )
            return Response(owner_serialized_data.data)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):

        owner_request_data = request.data

        owner_serialized_data = OwnerSerializer(
            data=owner_request_data,
            context={"request" : request}
        )

        if owner_serialized_data.is_valid ():

            owner_serialized_data.save()
            return Response (
                owner_serialized_data.data,
                status=status.HTTP_201_CREATED
            )

        return Response (
            owner_serialized_data.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    @method_decorator(csrf_exempt)
    def put(self, request, person_id = None, pet_id = None, *args, **kwargs):

        owner_request_data = request.data

        if not(person_id is None) and not(pet_id is None):

            owner_data = Owner.owners.get_by_person_id_and_pet_id(person_id, pet_id)

            if owner_data.exists():

                owner_serialized_data = OwnerSerializer(
                    owner_data.get(),
                    data=owner_request_data,
                    context={"request" : request}
                )

                if owner_serialized_data.is_valid ():

                    owner_serialized_data.save()
                    return Response (owner_serialized_data.data)

                return Response(
                    owner_serialized_data.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response (
            'An update request must include the person_id and pet_id parameters as part of the URL',
            status = status.HTTP_400_BAD_REQUEST
        )

    @method_decorator(csrf_exempt)
    def patch(self, request, person_id = None, pet_id = None, *args, **kwargs):

        owner_request_data = request.data

        if not(person_id is None) and not(pet_id is None):

            owner_data = Owner.owners.get_by_person_id_and_pet_id(person_id, pet_id)

            if owner_data.exists():

                owner_data = owner_data.get()

                # Note:
                #   - I could have done this in the update method of the serializer. I just wanted to implement it here
                #     to show a difference between the patch and put requests

                if not ('person_id' in owner_request_data):
                    owner_request_data['person_id'] = owner_data.person.id

                if not ('pet_id' in owner_request_data):
                    owner_request_data['pet_id'] = owner_data.pet.id

                owner_serialized_data = OwnerSerializer(
                    owner_data,
                    data=owner_request_data,
                    context={"request" : request}
                )

                if owner_serialized_data.is_valid ():

                    owner_serialized_data.save()
                    return Response (owner_serialized_data.data)

                return Response(
                    owner_serialized_data.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response (
            'An update request must include the person_id and pet_id parameters as part of the URL',
            status = status.HTTP_400_BAD_REQUEST
        )

    @method_decorator(csrf_exempt)
    def delete(self, request, person_id = None, pet_id = None, *args, **kwargs):

        owner_request_data = request.data

        if not(person_id is None) and not(pet_id is None):

            owner_data = Owner.owners.get_by_person_id_and_pet_id(person_id, pet_id)

            if owner_data.exists():
                owner_data.delete()
                return Response (status=status.HTTP_204_NO_CONTENT)

            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        return Response (
            'A delete request must include the person_id and pet_id parameters as part of the URL',
            status = status.HTTP_400_BAD_REQUEST
        )

import datetime

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# from oauth2_provider.contrib.rest_framework import OAuth2Authentication
# from oauth2_provider.contrib.rest_framework import TokenHasScope

from users_pets_api.models import Person

from users_pets_api.serializers import HyperlinkedPersonSerializer

# Note:
#   - Not all endpoints are needed, just wanted to show an example of HATEOAS here, so I duplicated the users and pets
#     endpoints to show an example of how they would look with a maybe very simple and very improvable HATEOAS approach


class HyperlinkedPersonAPIView (APIView):

#    authentication_classes = [OAuth2Authentication]
#    permission_classes     = [TokenHasScope]
#    required_scopes        = ['']

    @method_decorator(csrf_exempt)
    def get (self, request, id = None, *args, **kwargs):

        if id is None:
            person_data = Person.people.get_all()
            person_serialized_data = HyperlinkedPersonSerializer(
                person_data,
                many=True,
                context={"request": request}
            )
            return Response(person_serialized_data.data)

        person_data = Person.people.get_by_id(id)

        if person_data.exists():

            person_serialized_data = HyperlinkedPersonSerializer(
                person_data.get(),
                many=False,
                context={"request": request}
            )
            return Response(person_serialized_data.data)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):

        person_request_data = request.data

        person_serialized_data = HyperlinkedPersonSerializer(
            data=person_request_data,
            context={"request" : request}
        )
        person_serialized_data.date_joined = datetime.datetime.utcnow()

        if person_serialized_data.is_valid ():

            person_serialized_data.save()
            return Response (
                person_serialized_data.data,
                status=status.HTTP_201_CREATED
            )

        return Response (
            person_serialized_data.errors,
            status = status.HTTP_400_BAD_REQUEST
        )

    @method_decorator(csrf_exempt)
    def put(self, request, id = None, *args, **kwargs):

        person_request_data = request.data

        if not(id is None):

            person_data = Person.people.get_by_id(id)

            if person_data.exists():

                person_serialized_data = HyperlinkedPersonSerializer(
                    person_data.get(),
                    data=person_request_data,
                    context={"request" : request}
                )

                if person_serialized_data.is_valid ():

                    person_serialized_data.save()
                    return Response (person_serialized_data.data)

                return Response(
                    person_serialized_data.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response (
            'An update request must include the id parameter as part of the URL',
            status = status.HTTP_400_BAD_REQUEST
        )

    @method_decorator(csrf_exempt)
    def patch(self, request, id = None, *args, **kwargs):

        person_request_data = request.data

        if not(id is None):

            person_data = Person.people.get_by_id(id)

            if person_data.exists():

                person_data = person_data.get()

                # Note:
                #   - I could have done this in the update method of the serializer. I just wanted to implement it here
                #     to show a difference between the patch and put requests

                if not ('username' in person_request_data):
                    person_request_data['username'] = person_data.username

                if not ('phone_number' in person_request_data):
                    person_request_data['phone_number'] = person_data.phone_number.as_e164

                if not ('city' in person_request_data):
                    person_request_data['city'] = person_data.city

                person_serialized_data = HyperlinkedPersonSerializer(
                    person_data,
                    data=person_request_data,
                    context={"request" : request}
                )

                if person_serialized_data.is_valid ():

                    person_serialized_data.save()
                    return Response (person_serialized_data.data)

                return Response(
                    person_serialized_data.errors,
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

            person_data = Person.people.get_by_id(id)

            if person_data.exists():
                person_data.delete()
                return Response (status=status.HTTP_204_NO_CONTENT)

            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

        return Response (
            'A delete request must include the id parameter as part of the URL',
            status = status.HTTP_400_BAD_REQUEST
        )

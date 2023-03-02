from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# from oauth2_provider.contrib.rest_framework import OAuth2Authentication
# from oauth2_provider.contrib.rest_framework import TokenHasScope

from users_pets_api.models import Person

from users_pets_api.serializers import PersonSerializer


class PersonAPIView (APIView):

#    authentication_classes = [OAuth2Authentication]
#    permission_classes     = [TokenHasScope]
#    required_scopes        = ['']

    @method_decorator(csrf_exempt)
    def get (self, request, id = None, *args, **kwargs):

        if id is None:
            person_data = Person.people.get_all()
            person_serialized_data = PersonSerializer(
                person_data,
                many=True,
                context={"request": request}
            )
            return Response(person_serialized_data.data)

        person_data = Person.people.get_by_id(id)

        if person_data.exists():

            person_serialized_data = PersonSerializer(
                person_data.get(),
                many=False,
                context={"request": request}
            )
            return Response(person_serialized_data.data)

        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

from django.urls import path

from users_pets_api.views import HyperlinkedPersonAPIView
from users_pets_api.views import HyperlinkedPetAPIView
from users_pets_api.views import OwnerAPIView
from users_pets_api.views import PersonAPIView
from users_pets_api.views import PetAPIView
from users_pets_api.views import PetOwnerAPIView

urlpatterns = []

# Note:
#   - Not all endpoints are needed, just wanted to show an example of HATEOAS here, so I duplicated the users and pets
#     endpoints to show an example of how they would look with a maybe very simple and very improvable HATEOAS approach

users_pets_api_endpoint_views = [
    path(
        'owner/<int:person_id>/<int:pet_id>',
        OwnerAPIView.as_view(),
        name="owner-resource-by-person-id-and-pet-id-without-slash"
    ),
    path(
        'owner/<int:person_id>/<int:pet_id>/',
        OwnerAPIView.as_view(),
        name="owner-resource-by-person-id-and-pet-id-with-slash"
    ),
    path(
        'owner/<int:person_id>',
        PetOwnerAPIView.as_view(),
        name="owner-resource-by-person-id-without-slash"
    ),
    path(
        'owner/<int:person_id>/',
        PetOwnerAPIView.as_view(),
        name="owner-resource-by-person-id-with-slash"
    ),
    path(
        'owner/',
        OwnerAPIView.as_view(),
        name="owner-resource"
    ),
    path(
        'person/<int:id>',
        PersonAPIView.as_view (),
        name = "person-resource-by-id-without-slash"
    ),
    path(
        'person/<int:id>/',
        PersonAPIView.as_view(),
        name="person-resource-by-id-with-slash"
    ),
    path(
        'person/',
        PersonAPIView.as_view(),
        name="person-resource"
    ),
    path(
        'hyperlinked-person/<int:id>',
        HyperlinkedPersonAPIView.as_view(),
        name="hyperlinked-person-resource-by-id-without-slash"
    ),
    path(
        'hyperlinked-person/<int:id>/',
        HyperlinkedPersonAPIView.as_view(),
        name="hyperlinked-person-resource-by-id-with-slash"
    ),
    path(
        'hyperlinked-person/',
        HyperlinkedPersonAPIView.as_view(),
        name="hyperlinked-person-resource"
    ),
    path(
        'pet/<int:id>',
        PetAPIView.as_view(),
        name="pet-resource-by-id-without-slash"
    ),
    path(
        'pet/<int:id>/',
        PetAPIView.as_view(),
        name="pet-resource-by-id-with-slash"
    ),
    path(
        'pet/',
        PetAPIView.as_view(),
        name="pet-resource"
    ),
    path(
        'hyperlinked-pet/<int:id>',
        HyperlinkedPetAPIView.as_view(),
        name="hyperlinked-pet-resource-by-id-without-slash"
    ),
    path(
        'hyperlinked-pet/<int:id>/',
        HyperlinkedPetAPIView.as_view(),
        name="hyperlinked-pet-resource-by-id-with-slash"
    ),
    path(
        'hyperlinked-pet/',
        HyperlinkedPetAPIView.as_view(),
        name="hyperlinked-pet-resource"
    )
]

urlpatterns += users_pets_api_endpoint_views

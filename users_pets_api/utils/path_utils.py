import datetime
import uuid
import pathlib

from django.conf import settings


def get_pet_image_upload_path(instance, filename):
    filename_path = pathlib.Path(filename)

    to_upload_filename = uuid.uuid5 (
        uuid.NAMESPACE_DNS,
        filename_path.as_posix()
    )
    to_upload_extension = filename_path.suffix

    to_upload_filename = f"{settings.PET_IMAGES_MEDIA_BASE}/" \
                         f"{instance.chip_number}/" \
                         f"{to_upload_filename}" \
                         f"{to_upload_extension}"

    return to_upload_filename


def get_person_image_upload_path(instance, filename):
    filename_path = pathlib.Path(filename)

    to_upload_filename = uuid.uuid5 (
        uuid.NAMESPACE_DNS,
        filename_path.as_posix()
    )
    to_upload_extension = filename_path.suffix

    to_upload_filename = f"{settings.PERSON_IMAGES_MEDIA_BASE}/" \
                         f"{instance.username}/" \
                         f"{to_upload_filename}" \
                         f"{to_upload_extension}"

    return to_upload_filename

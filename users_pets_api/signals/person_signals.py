import pathlib
import shutil

from django.conf import settings


def delete_old_person_images(sender, instance, **kwargs):
    person_image_base_path = pathlib.Path(
        settings.MEDIA_ROOT, settings.PERSON_IMAGES_MEDIA_BASE, str(instance.username)
    )

    if (
        not(instance.person_image is None) and
        not(instance.person_image.name is None) and
        not(instance.person_image.name.strip()) == ''
    ):

        instance_person_image = pathlib.Path(instance.person_image.name)
        for existing_person_image_filename in person_image_base_path.glob('*'):
            if not (existing_person_image_filename.name == instance_person_image.name):
                existing_person_image_filename.unlink()

    elif person_image_base_path.exists():
        shutil.rmtree(person_image_base_path)


def delete_person_images_path(sender, instance, **kwargs):
    person_image_base_path = pathlib.Path(
        settings.MEDIA_ROOT, settings.PERSON_IMAGES_MEDIA_BASE, str(instance.username)
    )
    if person_image_base_path.exists():
        shutil.rmtree(person_image_base_path)

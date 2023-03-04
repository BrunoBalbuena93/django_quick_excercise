import pathlib
import shutil

from django.conf import settings


def delete_old_pet_images(sender, instance, **kwargs):
    pet_image_base_path = pathlib.Path(
        settings.MEDIA_ROOT, settings.PET_IMAGES_MEDIA_BASE, str(instance.chip_number)
    )

    if (
        not(instance.pet_image is None) and
        not(instance.pet_image.name is None) and
        not(instance.pet_image.name.strip()) == ''
    ):

        instance_pet_image = pathlib.Path(instance.pet_image.name)
        for existing_pet_image_filename in pet_image_base_path.glob('*'):
            if not (existing_pet_image_filename.name == instance_pet_image.name):
                existing_pet_image_filename.unlink()

    elif pet_image_base_path.exists():
        shutil.rmtree(pet_image_base_path)


def delete_pet_images_path(sender, instance, **kwargs):
    pet_image_base_path = pathlib.Path(
        settings.MEDIA_ROOT, settings.PET_IMAGES_MEDIA_BASE, str(instance.chip_number)
    )
    if pet_image_base_path.exists():
        shutil.rmtree(pet_image_base_path)

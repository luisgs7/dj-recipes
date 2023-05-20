import os

from django.db.models.signals import pre_delete
from django.dispatch import receiver

from recipes.models import Recipe


def delete_cover(instance):
    try:
        os.remove(instance.cover.path)
    except (ValueError, FileNotFoundError) as e:
        print(e)


@receiver(pre_delete, sender=Recipe)
def recipe_cover_delete(sender, instance, *args, **kwargs):
    old_recipe = Recipe.objects.get(pk=instance.pk)
    delete_cover(old_recipe)

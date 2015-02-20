from django.db.models.signals import post_save
from django.dispatch import receiver

from common.signal_helpers import task_signal

from .models import DataFile, HuId


@receiver(post_save, sender=HuId)
def post_save_cb(sender, instance, created, raw, update_fields, **kwargs):
    """
    Initiate retrieval of the data corresponding to an PGP huID.
    """
    task_signal(instance, created, raw, {'huid': instance.value}, DataFile)

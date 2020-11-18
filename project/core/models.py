from django.db import models
from django.utils.translation import gettext_lazy as _
# from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class TimeStampedModel(models.Model):
    # created_at = AutoCreatedField(_("created at"))
    # modified_at = AutoLastModifiedField(_("modified at"))
    created_at = models.DateTimeField(_("created at"), editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(_("modified at"), editable=False, auto_now=True)

    class Meta:
        abstract = True

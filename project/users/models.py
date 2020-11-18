from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    name = models.CharField(_("name"), blank=True, max_length=255)
    email_bound = models.BooleanField(_("email bound"), default=False)

import os
import sys

from pathlib import Path

import django

BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(BASE_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from blog.models import Category, Post, Tag, FriendLink
from django.contrib.auth.models import User


def clean_database():
    print("clean database")
    Post.objects.all().delete()
    Category.objects.all().delete()
    Tag.objects.all().delete()
    User.objects.all().delete()
    FriendLink.objects.all().delete()

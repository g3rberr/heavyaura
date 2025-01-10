from django.db import models
from django.urls import reverse


class Category:
    name = models.CharField(max_length=20,
                            unique=True)
    slug = models.SlugField

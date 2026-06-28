from django.db import models
from django.utils.text import slugify

from common.models import BaseModel
from accounts.models import User

# Create your models here.
class Organization(BaseModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=False)
    description = models.TextField(blank=True)
    logo = models.ImageField(upload_to="organization_logos/", blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_organizations')

    class meta:
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
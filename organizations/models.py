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
    
    def __str__(self):
        return self.name

class OrganizationMember(BaseModel):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        MANAGER = "MANAGER", "Manager"
        MEMBER = "MEMBER", "Member"

    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="members")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organizations")
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)
    joined_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "user"],
                name="unique_organization_member"
            )
        ]
    def __str__(self):
        return f"{self.user.email} - {self.organization.name}"
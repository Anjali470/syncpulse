from django.contrib import admin
from .models import Organization, OrganizationMember

# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "created_at",
    )
    search_fields =(
        "name",
        "owner__email",
    )
    prepopulated_fields = {
        "slug": ("name",)
    }

admin.site.register(OrganizationMember)
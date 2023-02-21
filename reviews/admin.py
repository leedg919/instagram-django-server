from django.contrib import admin
from .models import Review

@admin.register(Review)
class REviewAdmin(admin.ModelAdmin):
    list_display = (
        "caption",
    )

from django.contrib import admin
from .models import Registered_email


# Register your models here.
class Registered_emailAdmin(admin.ModelAdmin):
    list_display = ["email"]
    search_fields = ["email"]
    list_per_page = 10


admin.site.register(Registered_email, Registered_emailAdmin)

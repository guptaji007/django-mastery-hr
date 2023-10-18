from django.contrib import admin
from .models import Registered_email, Support, Message
from django.utils.html import format_html


# Register your models here.
class Registered_emailAdmin(admin.ModelAdmin):
    list_display = ["email"]
    search_fields = ["email"]
    list_per_page = 10


admin.site.register(Registered_email, Registered_emailAdmin)


class SupportAdmin(admin.ModelAdmin):
    list_filter = ["situation"]
    list_display = ["person", "email", "option", "created_at", "status", "_"]
    search_fields = ["person", "option"]
    list_per_page = 10

    # Function to change the icons (Done - Pending)
    def _(self, obj):
        if obj.situation == "Done":
            return True
        else:
            return False

    _.boolean = True

    # Function to color the text (Done - Pending)
    def status(self, obj):
        if obj.situation == "Done":
            color = "#28a745"
        else:
            color = "red"
        return format_html(
            '<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation)
        )

    status.allow_tags = True


admin.site.register(Support, SupportAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_filter = ["situation"]
    list_display = ["id", "created_at", "status", "_"]
    list_per_page = 10

    # Function to change the icons (Read - Unread)
    def _(self, obj):
        if obj.situation == "Read":
            return True
        else:
            return False

    _.boolean = True

    # Function to color the text (Read - Unread)
    def status(self, obj):
        if obj.situation == "Read":
            color = "#28a745"
        else:
            color = "red"
        return format_html(
            '<strong><p style="color: {}">{}</p></strong>'.format(color, obj.situation)
        )

    status.allow_tags = True


admin.site.register(Message, MessageAdmin)

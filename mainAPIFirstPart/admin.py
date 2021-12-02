from django.contrib import admin

from .models import IdentifierCode, LogMessage


admin.site.register(IdentifierCode)
admin.site.register(LogMessage)


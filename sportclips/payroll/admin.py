from django.contrib import admin

from .models import Reports, PayrollSettings

admin.site.register(PayrollSettings)
admin.site.register(Reports)

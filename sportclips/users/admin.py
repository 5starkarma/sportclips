from django.contrib import admin

from .models import User, Profile


class CustomUserAdmin(admin.ModelAdmin):
    fields = ('username', 'password', 'first_name', 'last_name',
              'email', 'phone', 'employee_type',
              'groups', 'user_permissions',
              'is_active', 'is_staff', 'is_superuser',
              'last_login', 'date_joined'
              )
    filter_horizontal = ('groups', 'user_permissions')


admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)

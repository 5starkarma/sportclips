from django.contrib import admin

from .models import Memo, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'created_date')


admin.site.register(Comment)
admin.site.register(Memo)

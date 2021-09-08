from django.contrib import admin
from .models import Key

class TodoAdmin(admin.ModelAdmin):
    list_display = ('key_name', 'key_description', 'key','date')


admin.site.register(Key)

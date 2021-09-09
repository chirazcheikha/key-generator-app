from django.contrib import admin
from .models import Key


# to display informations on django-admin rest api 
class TodoAdmin(admin.ModelAdmin):
    list_display = ('key_name', 'key_description', 'key','date')


admin.site.register(Key)

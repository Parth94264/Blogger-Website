from django.contrib import admin
from .models import Contact
# Register your models here.
from .models import *

admin.site.register(Blog)
admin.site.register(Blogger)



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email')
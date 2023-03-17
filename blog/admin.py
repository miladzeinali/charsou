from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('id','writer','title')
    search_fields = ('id','title','writer')

class WriterAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields = ('name','id')

admin.site.register(Post,PostAdmin)
admin.site.register(Writer,WriterAdmin)
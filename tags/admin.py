from django.contrib import admin
from .models import Tag, TageedItem

# Register your models here.
admin.site.register(Tag)
admin.site.register(TageedItem)
from django.contrib import admin

# Register your models here.

from .models import *

class TagTublerInline(admin.TabularInline):
    model = Tag


class PostAdmin(admin.ModelAdmin):
    inlines = [TagTublerInline]

admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)

from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
#admin.site.register (Post)

class MainappAdmin(SummernoteModelAdmin):
    list_display = ('id', 'cat', 'title', 'photo', 'document', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ('content',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Mainapp, MainappAdmin)
admin.site.register(Category, CategoryAdmin)

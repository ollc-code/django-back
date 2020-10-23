from django.contrib import admin
from .models import Reading

# Register your models here.

class ReadingAdmin(admin.ModelAdmin):
    model = Reading
    list_display = ('date','reading', 'book', 'content',)
    list_filter = ('date','reading', 'book', 'content',)

    search_fields = ('date',)
    ordering = ('date',)

admin.site.register(Reading, ReadingAdmin)
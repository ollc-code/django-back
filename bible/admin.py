from django.contrib import admin
from .models import Reading, ReadingVerse

# Register your models here.

class ReadingAdmin(admin.ModelAdmin):
    model = Reading
    list_display = ('date','reading', 'book',)
    list_filter = ('date','reading', 'book',)

    search_fields = ('date',)
    ordering = ('date',)


class ReadingVerseAdmin(admin.ModelAdmin):
    model = ReadingVerse
    list_display = ('reading','chapter', 'start_verse', 'end_verse',)
    list_filter = ('reading','chapter', 'start_verse', 'end_verse',)

    search_fields = ('reading', 'chapter',)
    ordering = ('reading', 'chapter', 'start_verse',)


admin.site.register(Reading, ReadingAdmin)
admin.site.register(ReadingVerse, ReadingVerseAdmin)
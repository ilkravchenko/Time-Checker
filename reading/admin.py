from django.contrib import admin
from .models import ReadingSession

# Register your models here.
class ReadingSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'started_at', 'ended_at', 'read_time', 'book')
    list_filter = ('user', 'book')


admin.site.register(ReadingSession, ReadingSessionAdmin)
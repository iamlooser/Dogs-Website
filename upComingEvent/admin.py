from django.contrib import admin
from upComingEvent.models import UpComingEvent
# Register your models here.


class UpComingEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'commit', 'uploaded_on', 'document')
admin.site.register(UpComingEvent, UpComingEventAdmin)

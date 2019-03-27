from django.contrib import admin
from event.models import Event,EventPhotos
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'date', 'views', 'commit', 'uploaded_on', 'document')
admin.site.register(Event, EventAdmin)


class EventPhotosAdmin(admin.ModelAdmin):
    list_display = ('event', 'time', 'url')
admin.site.register(EventPhotos, EventPhotosAdmin)

admin.site.site_header = 'My-Dog-Show'

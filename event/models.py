from django.db import models

# Create your models here.
from any_urlfield.models import AnyUrlField

class Event(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    date = models.DateField(null=True)
    commit = models.TextField(blank=False, null=False)
    views = models.IntegerField( default=0 )
    document = models.FileField(upload_to='Event/')
    uploaded_on = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __unicode__(self):
        return self.uploaded_on

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('date', 'title')
        managed = True
        db_table = "event_database"


class EventPhotos(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    url = AnyUrlField("URL", max_length=1000)
    time = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __str__(self):
        return self.event.title
    class Meta:
        ordering = ('event','time')
        verbose_name_plural = 'Event Photos'

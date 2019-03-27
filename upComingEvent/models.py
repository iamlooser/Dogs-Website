from django.db import models

# Create your models here.
# Create your models here.
class UpComingEvent(models.Model):
    title = models.CharField(max_length=50, null=False)
    date = models.DateField(null=True)
    commit = models.TextField(blank=False, null=False)
    document = models.FileField(upload_to='img_upComingEvent/')
    uploaded_on = models.DateTimeField(auto_now=False,auto_now_add=True)

    def __unicode__(self):
        return self.uploaded_on

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('date', 'uploaded_on')
        managed = True
        db_table = "event_upcoming_database"

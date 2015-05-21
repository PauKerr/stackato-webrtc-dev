from django.db import models
from time import gmtime, strftime
import shortuuid

def generate_storage_name(instance, filename):
    instance.filename = filename
    extension = filename.split('.')[-1]
    return "%s/%s.%s" % (strftime('%Y-%m-%d', gmtime()),
                         shortuuid.uuid(), extension)

class LogCollection(models.Model):
    received_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

class LogFile(models.Model):
    collection = models.ForeignKey(LogCollection)
    filename = models.CharField(max_length=1024)
    filetype = models.CharField(max_length=32)
    fileobj = models.FileField(upload_to=generate_storage_name)

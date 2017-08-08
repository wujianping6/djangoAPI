from django.db import models
from django.conf import settings
# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    name = models.CharField("Name", max_length=255)
    done = models.BooleanField("Done", default=False)
    date_created = models.DateTimeField("Date Created", auto_now_add=True)

    class Meta:
        verbose_name = u"Todo"
        verbose_name_plural = u"Todos"

    def __unicode__(self):
        return self.name
from django.db import models

# Create your models here.
class Define3(models.Model):
    type = models.CharField(max_length=3, blank=True, null=True)
    word = models.CharField(max_length=66, blank=True, null=True)
    rel = models.CharField(max_length=4, blank=True, null=True)
    definition = models.CharField(max_length=470, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'define3'

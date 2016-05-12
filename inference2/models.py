from django.db import models

# Create your models here.
class Define3(models.Model):
    extra = models.CharField(max_length=5, blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    word = models.CharField(max_length=66, blank=True, null=True)
    rel = models.CharField(max_length=4, blank=True, null=True)
    definition = models.CharField(max_length=470, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'define3'

class Input(models.Model):
    col1 = models.CharField(max_length=5, blank=True, null=True)
    col2 = models.CharField(max_length=500, blank=True, null=True)
    col3 = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'input'
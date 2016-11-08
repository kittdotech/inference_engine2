from django.db import models

# Create your models here.
class Archives(models.Model):
    archives_date = models.DateField()
    algorithm = models.CharField(max_length=300, blank=False, null=False)
    
    def __unicode__(self):
        return u'{0}, {1}'.format(self.archives_date,self.algorithm)

    class Meta:
        managed = True
        db_table = 'archives'

class Define3(models.Model):
    extra = models.CharField(max_length=5, blank=True, null=True)
    type = models.CharField(max_length=5, blank=True, null=True)
    word = models.CharField(max_length=66, blank=True, null=True)
    rel = models.CharField(max_length=4, blank=True, null=True)
    definition = models.CharField(max_length=1000, blank=True, null=True)
    archives = models.ForeignKey(Archives, on_delete=models.CASCADE)
    
    class Meta:
        managed = True
        db_table = 'define3'

class Input(models.Model):
    col1 = models.CharField(max_length=5, blank=True, null=True)
    col2 = models.CharField(max_length=1000, blank=True, null=True)
    col3 = models.CharField(max_length=300, blank=True, null=True)
    archives = models.ForeignKey(Archives, on_delete=models.CASCADE)

    class Meta:
        managed = True
        db_table = 'input'

class Output(models.Model):

    col1 = models.CharField(max_length=200, blank=True, null=True)
    col2 = models.CharField(max_length=1000, blank=True, null=True)
    col3 = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'output'


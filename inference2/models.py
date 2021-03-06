from django.db import models

# Create your models here.


class InstructionFile(models.Model):
    data = models.FileField(upload_to='./static/inference2/')

    def save(self, *args, **kwargs):
        super(InstructionFile, self).save(*args, **kwargs)
        filename = self.data.url


class Archives(models.Model):
    archives_date = models.DateField()
    algorithm = models.CharField(max_length=300, blank=False, null=False)

    def __unicode__(self):
        return u'{0}, {1}'.format(self.archives_date, self.algorithm)

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
    archives = models.ForeignKey(Archives)

    class Meta:
        managed = True
        db_table = 'output'
        verbose_name = "Argument"
        verbose_name_plural = "Arguments"


class Algorithm(models.Model):
    def validate_file_extension(value):
        from django.core.exceptions import ValidationError
        if not value.name.endswith('.py'):
            raise ValidationError(u'Only files with py extenstion are supported.')

    name = models.CharField(max_length=200)
    data = models.FileField(upload_to='./inference2/Proofs/',
                            validators=[])
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Algorithm, self).save(*args, **kwargs)

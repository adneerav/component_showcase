from django.db import models


# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=25, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/images/technology/', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'

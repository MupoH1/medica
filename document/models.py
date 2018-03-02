from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, default=None)
    description = models.TextField(max_length=90, blank=True, null=False, default=None)
    image = models.ImageField(upload_to='documents_images/')

    def __str__(self):
        return "%s " % self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

from django.db import models


class Document(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, default=None, verbose_name='Название')
    description = models.TextField(max_length=90, blank=True, null=False, default=None, verbose_name='Описание')
    image = models.ImageField(upload_to='documents_images/', verbose_name='Картинка')

    def __str__(self):
        return "%s " % self.name

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

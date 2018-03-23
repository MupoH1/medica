from django.db import models, transaction
from ckeditor_uploader.fields import RichTextUploadingField


class About(models.Model):
    title = models.CharField(max_length=64, blank=False, null=False, default=None, verbose_name='Заголовок')
    text = RichTextUploadingField(blank=True, null=False, default=None, verbose_name='Текст')
    is_active = models.BooleanField(default=True, unique=True, verbose_name='Активное')

    def __str__(self):
        return "%s " % self.title

    class Meta:
        verbose_name = 'Описание клиники'
        verbose_name_plural = 'Описание клиники'

    def get_image(self):
        return self.aboutimage_set.filter(is_active=True, is_main=True)

    def get_other_images(self):
        return self.aboutimage_set.filter(is_active=True).exclude(is_main=True)


class AboutImage(models.Model):
    clinic = models.ForeignKey('About', blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='about_images/', verbose_name='Фотография')
    is_main = models.BooleanField(default=False, verbose_name='Главная')
    is_active = models.BooleanField(default=True, verbose_name='Активная')

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = 'Фото клиники'
        verbose_name_plural = 'Фото клиники'

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.is_main:
            AboutImage.objects.filter(clinic=self.clinic, is_main=True).update(is_main=False)
        super(AboutImage, self).save(*args, **kwargs)


class WordRequisites(models.Model):
    file = models.FileField(upload_to='files/', verbose_name='Файл')
    is_actual = models.BooleanField(default=True, verbose_name='Актуален?')

    def __str__(self):
        return " %s " % self.file

    class Meta:
        verbose_name = 'Реквизиты для скачивания'
        verbose_name_plural = 'Реквизиты для скачивания'

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.is_actual:
            WordRequisites.objects.filter(file=self.file, is_actual=True).update(is_actual=False)
        super(WordRequisites, self).save(*args, **kwargs)

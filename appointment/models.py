from django.db import models


class Appointment(models.Model):
    full_name = models.CharField(max_length=64, blank=False, null=False, default=None, verbose_name='Имя')
    phone_number = models.CharField(max_length=90, blank=False, null=False, default=None, verbose_name='Телефон')
    email = models.EmailField(max_length=64, blank=True, null=False, default=None)
    comment = models.TextField(blank=True, null=False, default=None, verbose_name='Комментарий')
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата')

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'

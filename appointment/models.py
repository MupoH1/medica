from django.db import models


class Appointment(models.Model):
    full_name = models.CharField(max_length=64, blank=False, null=False, default=None)
    phone_number = models.CharField(max_length=90, blank=False, null=False, default=None)
    email = models.EmailField(max_length=64, blank=True, null=False, default=None)
    comment = models.TextField(blank=True, null=False, default=None)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = 'Запись на прием'
        verbose_name_plural = 'Записи на прием'

from django.db import models


class Review(models.Model):
    customer_name = models.CharField(max_length=64, blank=False, null=False, default=None, verbose_name='Имя клиента')
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата')
    review = models.TextField(blank=False, null=True, default=None, verbose_name='Отзыв')
    doctor = models.ForeignKey('employee.Doctor', blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Доктор')
    is_active = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return "Отзыв за %s " % self.date

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

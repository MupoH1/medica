from django.db import models


class Review(models.Model):
    customer_name = models.CharField(max_length=64, blank=False, null=False, default=None)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    review = models.TextField(blank=False, null=True, default=None)
    doctor = models.ForeignKey('employee.Doctor', blank=True, null=True, default=None, on_delete=models.CASCADE)
    is_active = models.BooleanField(blank=False, null=False, default=False)

    def __str__(self):
        return "Отзыв за %s " % self.date

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

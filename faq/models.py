from django.db import models


class Question(models.Model):
    curator = models.CharField(max_length=64, blank=True, null=True, default=None, verbose_name='Курирующий врач')
    question = models.TextField(max_length=90, blank=False, verbose_name='Вопрос')
    customer_name = models.CharField(max_length=32, blank=False, verbose_name='Имя клиента')
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name='Дата')
    department = models.ForeignKey('department.Department', blank=False, on_delete=models.CASCADE, verbose_name='Отделение')
    news = models.ForeignKey('news.News', blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='Ссылка на программу')

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

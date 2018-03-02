from django.db import models


class Question(models.Model):
    curator = models.CharField(max_length=64, blank=False, null=False, default=None)
    question = models.TextField(max_length=90, blank=False, null=False, default=None)
    customer_name = models.CharField(max_length=32, blank=False, null=False, default=None)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)
    department = models.ForeignKey('department.Department', blank=False, null=False, default=None, on_delete=models.CASCADE)
    news = models.ForeignKey('news.News', blank=False, null=False, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

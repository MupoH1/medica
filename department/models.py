from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, default=None, verbose_name='Название')
    short_name = models.CharField(max_length=24, blank=False, null=False, default='Кардиология', verbose_name='Короткое название')
    description = models.TextField(blank=False, null=False, default=None, verbose_name='Описание')
    image = models.ImageField(upload_to='department_images/', null=True, default=None, verbose_name='Картинка')
    icon = models.ImageField(upload_to='department_images/', null=True, default=None, verbose_name='Иконка')
    services_description = models.TextField(blank=False, null=False, default=None, verbose_name='Описание для списка отделений')
    consult_price = models.DecimalField(decimal_places=0, max_digits=6, blank=False, null=False, default=None, verbose_name='Цена консультации')
    consult_doctor = models.ForeignKey('employee.Doctor', blank=True, null=True, default=None, related_name='+', verbose_name='Консультирующий доктор')
    is_index_active = models.BooleanField(default=True, verbose_name='Показывать на главной')
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s " % self.name

    class Meta:
        verbose_name = 'Отделение'
        verbose_name_plural = 'Отделения'

    def get_doctors(self):
        return self.doctor_set.all()

    def get_prices(self):
        return self.pricelist_set.all()

    def get_absolute_url(self):
        return "/department/%s/" % self.id

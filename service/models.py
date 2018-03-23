from django.db import models, transaction


class Service(models.Model):
    service_name = models.CharField(max_length=64, blank=False, null=False, default=None, verbose_name='Название блока')

    def __str__(self):
        return " %s " % self.service_name

    class Meta:
        verbose_name = 'Блок услуг или исследований'
        verbose_name_plural = 'Блоки услуг или исследований'

    def get_items(self):
        return self.pricelist_set.all()


class PriceList(models.Model):
    item_name = models.CharField(max_length=64, blank=False, null=False, default=None, verbose_name='Название')
    item_price = models.DecimalField(decimal_places=0, max_digits=10, blank=False, null=False, default=None, verbose_name='цена')
    item_time = models.CharField(max_length=64, blank=False, null=False, default=None, verbose_name='Время выполнения')
    service = models.ForeignKey('Service', blank=False, null=False, default=None, on_delete=models.CASCADE, verbose_name='Блок услуг или исследований')
    department = models.ForeignKey('department.Department', blank=True, null=True, default=None,
                                   on_delete=models.CASCADE, verbose_name='Отделение')

    def __str__(self):
        return " %s " % self.item_name

    class Meta:
        verbose_name = 'Позиция прайса'
        verbose_name_plural = 'Позиции прайса'


class ExcellPrice(models.Model):
    file = models.FileField(upload_to='files/', verbose_name='Файл')
    is_actual = models.BooleanField(default=True, verbose_name='Актуален?')

    def __str__(self):
        return " %s " % self.file

    class Meta:
        verbose_name = 'Прайс для скачивания'
        verbose_name_plural = 'Прайс для скачивания'

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.is_actual:
            ExcellPrice.objects.filter(file=self.file, is_actual=True).update(is_actual=False)
        super(ExcellPrice, self).save(*args, **kwargs)

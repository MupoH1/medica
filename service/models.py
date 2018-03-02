from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=64, blank=False, null=False, default=None)

    def __str__(self):
        return " %s " % self.service_name

    class Meta:
        verbose_name = 'Блок услуг или исследований'
        verbose_name_plural = 'Блоки услуг или исследований'

    def get_items(self):
        return self.pricelist_set.all()


class PriceList(models.Model):
    item_name = models.CharField(max_length=64, blank=False, null=False, default=None)
    item_price = models.DecimalField(decimal_places=0, max_digits=10, blank=False, null=False, default=None)
    item_time = models.CharField(max_length=64, blank=False, null=False, default=None)
    service = models.ForeignKey('Service', blank=False, null=False, default=None, on_delete=models.CASCADE)
    department = models.ForeignKey('department.Department', blank=True, null=True, default=None,
                                   on_delete=models.CASCADE)

    def __str__(self):
        return " %s " % self.item_name

    class Meta:
        verbose_name = 'Позиция прайса'
        verbose_name_plural = 'Позиции прайса'

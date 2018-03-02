from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, default=None)
    short_name = models.CharField(max_length=24, blank=False, null=False, default='Кардиология')
    description = models.TextField(blank=False, null=False, default=None)
    image = models.ImageField(upload_to='department_images/', null=True, default=None)
    icon = models.ImageField(upload_to='department_images/', null=True, default=None)
    services_description = models.TextField(blank=False, null=False, default=None)
    consult_price = models.DecimalField(decimal_places=0, max_digits=6, blank=False, null=False, default=None)
    consult_doctor = models.ForeignKey('doctor_card.Doctor', blank=True, null=True, default=None, related_name='+')
    is_index_active = models.BooleanField(default=True)
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
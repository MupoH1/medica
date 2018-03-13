from django.db import models


class Employee(models.Model):
    DIRECTOR = 'DR'
    MAIN_DOCTOR = 'MD'
    ADMINISTRATION = 'AD'
    POSITION = (
        (DIRECTOR, 'Директор'),
        (MAIN_DOCTOR, 'Главный врач'),
        (ADMINISTRATION, 'Администратор'),
    )

    full_name = models.CharField(max_length=64, blank=False, null=False, default=None)
    position = models.CharField(max_length=2, choices=POSITION, default=ADMINISTRATION)
    image = models.ImageField(upload_to='employees_images/', blank=False, null=False, default=None)
    is_displayed = models.BooleanField(default=False)

    def __str__(self):
        return "%s " % self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

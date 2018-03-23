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

    full_name = models.CharField(max_length=64, blank=False, null=False, default=None, verbose_name='Имя')
    position = models.CharField(max_length=2, choices=POSITION, default=ADMINISTRATION, verbose_name='Должность')
    image = models.ImageField(upload_to='employees_images/', blank=False, null=False, default=None, verbose_name='Картинка')
    is_displayed = models.BooleanField(default=False, verbose_name='Отображать')

    def __str__(self):
        return "%s " % self.full_name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class Doctor(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, default=None, verbose_name='Имя')
    position = models.CharField(max_length=64, blank=False, null=False, default=None, verbose_name='Должность')
    image = models.ImageField(upload_to='doctors_images/', blank=False, null=True, default=None, verbose_name='Картинка')
    department = models.ForeignKey('department.Department', blank=False, null=True, default=None, verbose_name='Отделение')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s " % self.name

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def get_textfields(self):
        return self.doctortextfield_set.all()

    def get_rewiews(self):
        return self.review_set.all()

    def get_seniority(self):
        return self.seniority_set.all()

    def get_absolute_url(self):
        return "/doctor-card/%s/" % self.id


class DoctorTextField (models.Model):
    doctor = models.ForeignKey(Doctor, blank=True, null=True, default=None, verbose_name='Врач')
    description = models.TextField(blank=False, null=True, default=None, verbose_name='Описание заслуги')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = 'Заслуга'
        verbose_name_plural = 'Заслуги'


class Seniority (models.Model):
    seniority = models.CharField(max_length=256, blank=False, null=True, default=None, verbose_name='Описание')
    doctor = models.ForeignKey(Doctor, blank=True, null=True, default=None)

    def __str__(self):
        return "Стаж врача %s " % self.doctor.name

    class Meta:
        verbose_name = 'Статья стажа'
        verbose_name_plural = 'Статьи стажа'


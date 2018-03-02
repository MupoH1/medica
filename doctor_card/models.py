from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False, default=None)
    position = models.CharField(max_length=64, blank=False, null=False, default=None)
    image = models.ImageField(upload_to='doctors_images/', blank=False, null=True, default=None)
    department = models.ForeignKey('department.Department', blank=False, null=True, default=None)
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


class DoctorTextField (models.Model):
    doctor = models.ForeignKey(Doctor, blank=True, null=True, default=None)
    description = models.TextField(blank=False, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = 'Заслуга'
        verbose_name_plural = 'Заслуги'


class Seniority (models.Model):
    seniority = models.CharField(max_length=256, blank=False, null=True, default=None)
    doctor = models.ForeignKey(Doctor, blank=True, null=True, default=None)

    def __str__(self):
        return "Стаж врача %s " % self.doctor.name

    class Meta:
        verbose_name = 'Статья стажа'
        verbose_name_plural = 'Статьи стажа'


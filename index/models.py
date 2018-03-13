# from ckeditor_uploader.fields import RichTextUploadingField
# from django.db import models
#
#
# class Slide(models.Model):
#     title = models.CharField(max_length=24, blank=False, null=False, default=None)
#     text = RichTextUploadingField(max_length=24, blank=False, null=False, default=None)
#     image = models.ImageField(upload_to='slider_images/', null=True, default=None)
#     is_active = models.BooleanField(default=True)
#
#     def __str__(self):
#         return "%s " % self.title
#
#     class Meta:
#         verbose_name = 'Слайд'
#         verbose_name_plural = 'Слайды на главной'

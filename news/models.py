from django.db import models, transaction
from ckeditor_uploader.fields import RichTextUploadingField



class News(models.Model):
    title = models.CharField(max_length=64, blank=False, null=False, default=None)
    preview = models.TextField(blank=True, null=False, default=None)
    date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "%s " % self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def get_image(self):
        return self.newsimage_set.filter(is_active=True, is_main=True)

    def get_other_images(self):
        return self.newsimage_set.filter(is_active=True).exclude(is_main=True)

    def get_textfields(self):
        return self.newstextfield_set.all()


class NewsTextField(models.Model):
    news = models.ForeignKey('News', blank=True, null=True, default=None, on_delete=models.CASCADE)
    article = models.CharField(max_length=64, blank=False, null=False, default=None)
    text = RichTextUploadingField(blank=True, null=False, default=None,)

    def __str__(self):
        return "%s " % self.article

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки статьи'



class NewsImage(models.Model):
    news = models.ForeignKey('News', blank=True, null=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s " % self.id

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки новостей'

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.is_main:
            NewsImage.objects.filter(news=self.news, is_main=True).update(is_main=False)
        super(NewsImage, self).save(*args, **kwargs)

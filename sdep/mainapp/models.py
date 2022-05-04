from django.db import models
from django.urls import reverse


class Mainapp(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")  # максимальна довжина заголовку 255 символів
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL")  # unique=True це унакальна url-адреса
    content = models.TextField(blank=False, verbose_name="Текст")  # поле не може бути порожнім
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Зображення")  # завантажується до
    document = models.FileField(blank=True, upload_to="documents/%Y/%m/%d/", verbose_name="Додаток")  # завантажуэться до
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Створено")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Змінено")
    is_published = models.BooleanField(default=True, verbose_name="Публікація")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категорія")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'допис головного додатку'
        verbose_name_plural = 'дописи головного додатку'
        ordering = ['-time_create', 'title']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категорія")
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            verbose_name="URL")  # unique=True це унакальна url-адреса

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['id']

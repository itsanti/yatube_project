from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Имя', max_length=200)
    slug = models.SlugField('Адрес', max_length=100, unique=True)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name='Сообщество',
    )

    class Meta:
        ordering = ['-pub_date']

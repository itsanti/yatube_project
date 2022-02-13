from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Post(models.Model):
    # Тип: TextField
    text = models.TextField()

    # Тип поля: DateTimeField, для хранения даты и времени;
    # параметр auto_now_add определяет, что в поле будет автоматически
    # подставлено время и дата создания новой записи
    pub_date = models.DateTimeField(auto_now_add=True)

    # Тип: ForeignKey, ссылка на модель User
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )

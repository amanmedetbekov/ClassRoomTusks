from django.db import models
from django.contrib.auth import get_user_model

from product.models import Product

User = get_user_model()


class Review(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор'
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Описание')
    rating_choices = [
        (1, '⭐️'),
        (2, '⭐️⭐️'),
        (3, '⭐️⭐️⭐️'),
        (4, '⭐️⭐️⭐️⭐️'),
        (5, '⭐️⭐️⭐️⭐️⭐️'),
    ]
    rating = models.IntegerField(
        choices=rating_choices, verbose_name='Рейтинг')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Оценка'
        verbose_name_plural = 'Оценки'

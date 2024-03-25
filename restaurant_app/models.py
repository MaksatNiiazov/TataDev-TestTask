from django.contrib.auth.models import User
from django.db import models
from restaurant_app.utils import get_location


class Restaurant(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название")
    address = models.TextField(verbose_name="Адрес")
    description = models.TextField(blank=True, verbose_name="Описание")
    latitude = models.FloatField(verbose_name="Широта", null=True, blank=True)
    longitude = models.FloatField(verbose_name="Долгота", null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.latitude or not self.longitude:
            latitude, longitude = get_location(self.address)
            self.latitude = latitude
            self.longitude = longitude
        super().save(*args, **kwargs)


class Review(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Ресторан"
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь"
    )
    rating = models.PositiveSmallIntegerField(verbose_name="Рейтинг")
    comment = models.TextField(verbose_name="Комментарий")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.rating} - {self.restaurant.name} - {self.user.username}"

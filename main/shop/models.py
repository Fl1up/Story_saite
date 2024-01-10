from django.db import models


# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    price = models.IntegerField(verbose_name="Цена")
    image = models.ImageField(verbose_name='Фото')
    description = models.TextField(max_length=550, verbose_name="Описание")

    def __str__(self):
        return f"{self.name} | {self.price} | {self.image}"

    class Meta:
        verbose_name = "Магазин"
        verbose_name_plural = "Магазины"


class Calculation(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
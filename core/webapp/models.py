from django.db import models
from django.db.models import TextChoices


class ProductsChoice(TextChoices):
    SMARTPHONE = 'SmartPhone', 'Смартфоны'
    TABLETS = 'Tablets', 'Планшеты'
    PC = 'PC', 'ПК'
    NOTEBOOK = 'NoteBook', 'Ноутбук'


class Products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование товара')
    description = models.TextField(max_length=2000, null=True, blank=False, verbose_name='Описание товара')
    img = models.CharField(max_length=300, null=False, blank=False, verbose_name='Фото')
    category = models.CharField(choices=ProductsChoice.choices, default='Other', max_length=60, verbose_name='Категория')
    remainder = models.IntegerField(verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name='Стоимость')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    def __str__(self):
        return self.name, self.description, self.category

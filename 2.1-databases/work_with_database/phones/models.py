from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=1)
    image = models.CharField(max_length=200)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200)

# ЭТО УДАЛИТЬ ПЕРЕД сдачей ДЗ:
# В файле models.py нашего приложения создаем модель Phone с полями
# id, name, price, image, release_date, lte_exists и slug. Поле id - должно быть основным ключом модели.
# Значение поля slug должно устанавливаться слагифицированным значением поля name.
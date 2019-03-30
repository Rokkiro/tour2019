from django.db import models
from django.urls import reverse
from datetime import datetime


class Band(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myblog:persons', kwargs={'pk': self.pk})


class Member(models.Model):
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " - " + self.band.name


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " - " + self.country.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Currency(models.Model):
    name = models.CharField(max_length=100)
    rate = models.FloatField(default=0.0)
    date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name + " (" + str(self.date) + ") = " + str(self.rate)


class Sign(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class Money(models.Model):
    date = models.DateField(default=datetime.now, blank=True,  verbose_name='Дата')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True,  verbose_name='ФИО')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE,  verbose_name='Валюта')
    city = models.ForeignKey(City, on_delete=models.CASCADE,  verbose_name='Город')
    sign = models.ForeignKey(Sign, on_delete=models.CASCADE,  verbose_name='Приход\Расход')
    amount_cur = models.FloatField(default=0.0, blank=True,  verbose_name='Сумма (в валюте)')
    comment = models.CharField(max_length=300, default='', blank=True,  verbose_name='Комментарий')

    def __str__(self):
        return self.sign.symbol + str(self.get_amount_ru()) + " руб. " + self.category.name + " в " + self.city.name

    def get_amount_ru(self):
        return float(round(self.currency.rate * self.amount_cur, 2))

<<<<<<< HEAD
    def get_date_of_row(self):
        return self.date.strftime("%d-%m-%y")
=======
    def get_date(self):
        return self.date.strftime("%d/%m")

    def get_amount_cur(self):
        return str(self.amount_cur) + " " + self.currency.name

>>>>>>> 13eef93d9354183026c45e3aab371adffe5d01cb






from django.db import models
from django.urls import reverse


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
    rate = models.IntegerField()

    def __str__(self):
        return self.name


class Sign(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=1)

    def __str__(self):
        return self.name


class Money(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    sign = models.ForeignKey(Sign, on_delete=models.CASCADE)
    amount_ru = models.IntegerField(default=0, blank=True)
    amount_cur = models.IntegerField(default=0, blank=True)
    comment = models.CharField(max_length=300, default='', blank=True)

    def __str__(self):
        return self.sign.symbol + str(self.amount_ru) + " руб. " + self.category.name + " в " + self.city.name




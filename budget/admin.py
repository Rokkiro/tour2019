from django.contrib import admin

from django.contrib import admin
from .models import Band, Member, Country, City, Category, Currency, Sign, Money

admin.site.register(Band)
admin.site.register(Member)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Category)
admin.site.register(Currency)
admin.site.register(Sign)
admin.site.register(Money)


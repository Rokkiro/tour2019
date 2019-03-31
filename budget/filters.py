import django_filters
from budget.models import Money

class MoneyFilter(django_filters.FilterSet):

    class Meta:

        model = Money
<<<<<<< HEAD
        fields = ['sign','date','currency','category', 'city','member']
=======
        fields = ['sign', 'date', 'currency', 'category', 'city']
>>>>>>> 53b13ff5c7a52f7005afc485ce73e779156d76bd

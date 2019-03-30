import django_filters
from budget.models import Money

class MoneyFilter(django_filters.FilterSet):

    class Meta:

        model = Money
<<<<<<< HEAD
        fields = ['sign','date','currency','category', 'city','member']
=======
        fields = ['sign','date','currency','category', 'city']
>>>>>>> 13eef93d9354183026c45e3aab371adffe5d01cb

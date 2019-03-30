from django.views import generic
from budget.models import Money
from .filters import MoneyFilter
from django.shortcuts import redirect
from django.db.models import Sum


class IndexView(generic.ListView):
    template_name = 'budget/index.html'

    def get_queryset(self):
        return Money.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f_qs = MoneyFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = f_qs

        amount_ru_sum = 0
        for money in f_qs.qs:
            amount_ru_sum += money.amount_cur * money.currency.rate
        context['amount_ru_sum'] = amount_ru_sum

        return context


class CashView(generic.ListView):
    template_name = 'budget/cash.html'

    def get_queryset(self):
        return Money.objects.filter(category__name='cash')


def adminView(request):
    response = redirect('/admin/')
    return response


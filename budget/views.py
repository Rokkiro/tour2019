from django.views import generic
from budget.models import Money
from .filters import MoneyFilter


class IndexView(generic.ListView):
    template_name = 'budget/index.html'

    def get_queryset(self):
        return Money.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = MoneyFilter(self.request.GET, queryset=self.get_queryset())
        return context



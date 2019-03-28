from django.shortcuts import redirect

def BudgetView(request):
    response = redirect('/budget/')
    return response
from django.shortcuts import render
from django.template import loader

def budget(request):
    return render(request, 'budget/pricing-table.html', {})


from django.shortcuts import render
from django.template import loader

def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {})


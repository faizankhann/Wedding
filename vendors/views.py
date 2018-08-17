from django.shortcuts import render
from django.template import loader

def vendor(request):
    return render(request, 'vendors/vendor.html', {})


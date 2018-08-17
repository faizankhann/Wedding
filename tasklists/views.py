from django.shortcuts import render
from django.template import loader

#from tasklists.models import check, guest


def checklist(request):
    return render(request, 'tasklists/to-do-list.html', {})

def guestlist(request):
    return render(request, 'tasklists/guest-list.html', {})



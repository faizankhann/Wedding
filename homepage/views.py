from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from django.http import HttpResponsePermanentRedirect

def home(request):
    return render(request, 'homepage/index.html', {})


def contact(request):
    return render(request, 'homepage/contact.html', {})


def blog(request):
    return render(request, 'homepage/blog.html', {})


def about(request):
    return render(request, 'homepage/about.html', {})


def guest(request):
    return render(request, '../../tasklists/templates/tasklists/guest-list.html', {})


def help1(request):
    return render(request, 'homepage/help.html', {})


def checklist(request):
    return render(request, '../../tasklists/templates/tasklists/to-do-list.html', {})


def budget(request):
    return render(request, '../../budget/templates/budget/budget-planner.html', {})
from django.shortcuts import render
from django.template import loader
from login.models import Client
from django.shortcuts import redirect



def login(request):
    if (request.method == "POST"):
        p = Client.objects.filter(email = request.POST["email"], password = request.POST["password"])

        if len(p) > 0:
            request.session['email'] = p[0].email
            return redirect('dashboard')
        else:
            pass
    else:
        if 'email' in request.session:
            return redirect('dashboard')


    return render(request, 'login/register.html', {})

def logout(request):
    del request.session['email']
    return redirect("login")


def register(request):
    added = None

    if (request.method == 'POST'):
        c = Client(
            first_name=request.POST['fname'],
            last_name=request.POST['lname'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        c.save()
        added = c.id
    return render(request, 'login/register.html', {'id': added})

def password(request):
    return render(request, 'register.html', {})

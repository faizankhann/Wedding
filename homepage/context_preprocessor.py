from django.shortcuts import redirect


def auth(request):
    if 'email' in request.session:

        return {
            'logged_in': True
        }



    return {
        'logged_in': False
    }


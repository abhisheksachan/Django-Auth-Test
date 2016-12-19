from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    """Simple view for teting."""
    user = authenticate(username='sachan4894', password='abhishek')

    if user is not None:
        login(request, user)
        return HttpResponse("User Authenticated !")
    else:
        return HttpResponse("User not Authenticated !")

    if request.user.is_authenticated:
        return HttpResponse("User Authenticated !")
    else:
        return HttpResponse("User not Authenticated !")


def logout_view(request):
    """Simple view for teting."""
    print "logout", logout(request)
    return HttpResponse("User Logged out !")


@login_required(login_url='/login/')
def simple_view(request):
    """Simple view for teting."""
    return HttpResponse("A Simple View!")

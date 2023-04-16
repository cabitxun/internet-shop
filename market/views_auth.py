from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "login.html", context={"message": "Wrong username or password"})
        login(request, user)
        return HttpResponseRedirect("/")

    return render(request, "login.html")


def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return HttpResponseRedirect("/")

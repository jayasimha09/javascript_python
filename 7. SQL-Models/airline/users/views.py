from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

def login_view(request):
    if request.method == "post":
        username = request.post["username"]
        password = request.post["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login_view.html", {
                "context": "Invalid Credentials, please try with right creds!"
            })

def logout_view(request):
    return render(request, "users/logout_view.html")
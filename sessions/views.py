from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods
from django.contrib.auth import authenticate, login, logout as logout_user
from django.contrib import messages

# Create your views here.
@require_POST
def create(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(username=username, password=password)
    if user:
        login(request,user)
        messages.success(request,"Login successful.")
        return redirect("articles:index")
    else:
        messages.error(request,"Login unsuccessful.")
        return render(request,"sessions/new.html")
    

def new(request):
    return render(request, "sessions/new.html")

@require_http_methods(["DELETE"])
@require_POST
def logout(request):
    if request.POST["_method"]=="delete":
        logout_user(request)
        return redirect("sessions/new.html")
    else:
        return render(request,"articles:index")

    
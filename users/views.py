from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import UserForm

# Create your views here.
def create(request):
    if request.POST:
        form = UserForm(request.POST)
        form.save()
        return redirect("articles:index")
    else:
        return redirect("users:new")

def new(request):
    form = UserForm()
    return render(request, "users/new.html",{"form":form})
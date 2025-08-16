from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib import messages

# Create your views here.
def create(request):
    if request.POST:
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Register successful!")
            return redirect("articles:index")
        else:
            return render(request,'users/new.html',{"form":form})           
    else:
        return redirect("users:new")

def new(request):
    form = UserForm()
    return render(request, "users/new.html",{"form":form})
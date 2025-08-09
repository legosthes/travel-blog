from django.shortcuts import render
from .forms import ArticleForm
from django.views.decorators.http import require_POST


# Create your views here.
@require_POST
def index(request):
    form = ArticleForm(request.POST)
    form.save()

    return render(request, "articles/index.html")


def new(request):
    form = ArticleForm(request.POST)
    return render(request, "articles/new.html", {"form": form})

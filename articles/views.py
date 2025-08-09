from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article
from django.views.decorators.http import require_POST


# Create your views here.
def index(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        form.save()
        return redirect("articles:index")
    else:
        articles = Article.objects.filter(is_published=True).order_by("-published_at")
        return render(request, "articles/index.html", {"articles": articles})


def new(request):
    form = ArticleForm(request.POST)
    return render(request, "articles/new.html", {"form": form})


def detail(request, id):
    article = Article.objects.get(pk=id)
    if request.POST:
        if request.POST["_method"]=="patch":
            form = ArticleForm(request.POST,instance=article)
            form.save()
            return redirect("articles:detail", article.id)
        if request.POST["_method"]=="delete":
            article.delete()
            return redirect("articles:index")
    else:
        return render(request, "articles/detail.html", {"article": article})


def edit(request, id):
    article = Article.objects.get(pk=id)
    form = ArticleForm(instance=article)
    return render(request, "articles/edit.html",{"article":article,"form":form})


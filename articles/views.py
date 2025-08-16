from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article, Comment
from django.views.decorators.http import require_POST
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        form.save()
        messages.success(request,"Article created.")
        return redirect("articles:index")
    else:
        articles = Article.objects.filter(is_published=True).order_by("-published_at")
        return render(request, "articles/index.html", {"articles": articles})

@login_required
def new(request):
    form = ArticleForm(request.POST)
    return render(request, "articles/new.html", {"form": form})


def detail(request, id):
    article = Article.objects.get(pk=id)
    if request.POST and request.user.is_authenticated:
        if request.POST["_method"] == "patch":
            form = ArticleForm(request.POST, instance=article)
            form.save()
            messages.success(request,"Article saved.")
            return redirect("articles:detail", article.id)
        if request.POST["_method"] == "delete":
            article.delete()
            messages.error(request,"Article deleted.")
            return redirect("articles:index")
    else:
        # 顯示留言表格
        comment_form = CommentForm()
        # 顯示已經貼出來的留言
        comments = article.comment_set.filter(deleted_at__isnull=True).order_by(
            "-published_at"
        )
        # render出整個detail的頁面
        return render(
            request,
            "articles/detail.html",
            {"article": article, "form": comment_form, "comments": comments},
        )

@login_required
def edit(request, id):
    article = Article.objects.get(pk=id)
    form = ArticleForm(instance=article)
    return render(request, "articles/edit.html", {"article": article, "form": form})

@login_required
@require_POST
def create(request, id):
    # 得到我現在所在的article id
    article = Article.objects.get(pk=id)
    # 得到我request.POST傳進來的form
    form = CommentForm(request.POST)
    # 先暫存form
    comment = form.save(commit=False)
    # 把article存給comment的article欄位（因為request.POST並沒有傳進這個資訊）
    comment.article = article
    # 儲存comment
    comment.save()
    # 導向detail頁面
    return redirect("articles:detail", article.id)

@login_required
@require_POST
def delete_comment(request, id):
    comment = Comment.objects.get(pk=id)
    comment.deleted_at = datetime.now()
    comment.save()
    return redirect("articles:detail", comment.article_id)

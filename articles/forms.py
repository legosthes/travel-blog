from .models import Article
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "is_published"]
        labels = {"title": "Title", "content": "Content", "is_published": "Publish"}
        widgets = {
            "title": TextInput(attrs={"class": "input w-full"}),
            "content": Textarea(attrs={"class": "textarea w-full", "rows": 10}),
            "is_published": CheckboxInput(attrs={"class": "checkbox"}),
        }

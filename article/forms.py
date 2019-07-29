from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):

    title = forms.CharField(label='Название поста', max_length=500, required=True, widget=forms.TextInput({

    }))

    body = forms.CharField(
        label='Текст поста',
        widget=forms.Textarea({

        }),
        required=True,
    )

    class Meta:
        model = Article
        fields = ['title', 'body']
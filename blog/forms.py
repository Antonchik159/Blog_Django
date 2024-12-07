from .models import Post, Author, Comment
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, FileInput, Select, HiddenInput

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "image", "author"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок посту'
            }),
            "content": Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Вміст'
            }),
            "image": FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            "author": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            })
            # "published_date": DateTimeInput(attrs={
            #     'class': "form-control",
            #     'type': 'datetime-local',
            # })
        }

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["name", "bio"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Як звати автора?'
            }),
            "bio": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Біо'
            })
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["post", "author_name", "text"]
        widgets = {
            "post": HiddenInput(),
            "author_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ім’я'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'текст коментаря',
                'style': 'height: 100px;'
            })
        }
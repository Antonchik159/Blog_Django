from .models import Post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок посту'
            }),
            "content": Textarea(attrs={
                'class': "form-control",
                'placeholder': 'Вміст'
            }),
            # "published_date": DateTimeInput(attrs={
            #     'class': "form-control",
            #     'type': 'datetime-local',
            # })
        }
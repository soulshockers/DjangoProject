from django import forms

from .models import Category, Post

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {'name': ''}

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {'title': '', 'content': ''}
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}
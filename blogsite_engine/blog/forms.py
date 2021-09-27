from django import forms
from .models import *



class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_text', 'category', 'author']
        widgets = {
            'post_title': forms.Textarea(attrs={'cols': 95, 'rows': 2}),
            'post_text': forms.Textarea(attrs={'cols': 95, 'rows': 10}),
        }


class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'comment_text': forms.Textarea(attrs={'cols': 95, 'rows': 10}),
        }


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
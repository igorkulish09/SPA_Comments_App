from captcha.fields import ReCaptchaFields
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ['user_name', 'email', 'text']

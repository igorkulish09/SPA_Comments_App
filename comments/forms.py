from django import forms
from .models import Comment
# from  captcha.forms import reCuatchaFields

class CommentForm(forms.ModelForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ['user_name', 'email', 'text']

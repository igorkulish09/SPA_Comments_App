from django import forms
from .models import Comment
# from  captcha.forms import reCuatchaFields
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

class CommentForm(forms.ModelForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = Comment
        fields = ['user_name', 'email', "captcha",'text']


@deconstructible
class FileSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        if value.size > self.max_size * 1024:
            raise ValidationError(f'Розмір файлу повинен бути не більше {self.max_size} кБ.')


file = forms.FileField(validators=[FileSizeValidator(max_size=100)])

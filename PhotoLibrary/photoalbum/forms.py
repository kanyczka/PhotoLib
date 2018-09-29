from django import forms
from django.core.validators import EmailValidator, URLValidator
# from .models import
from photoalbum.models import Photo


class LoginForm(forms.Form):
    username = forms.CharField(max_length=64, required=True)
    password = forms.CharField(max_length=64, required=True, widget=forms.PasswordInput)


class ShowAllPhotosForm(forms.Form):
    path = forms.ImageField()
    creation_date = forms.DateTimeField()
    user = forms.CharField()


class AddPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

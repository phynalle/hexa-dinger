import datetime

from django import forms

class LoginForm(forms.Form):
    user = forms.CharField(max_length=100)
    passwd = forms.CharField(max_length=100, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    user = forms.CharField(max_length=100)
    passwd = forms.CharField(max_length=100, widget=forms.PasswordInput)
    email = forms.EmailField()

    name = forms.CharField(max_length=32)
    birthday = forms.DateField(initial=datetime.date.today)
    intro = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(max_length=11)



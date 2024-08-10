from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django import forms


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='', max_length=50,
                                widget=forms.TextInput(attrs=
                                                       {'class': 'form-control','name': 'FirstName',
                                                        'placeholder': 'نام خود را وارد کنید'}))
    last_name = forms.CharField(label='', max_length=50,
                               widget=forms.TextInput(attrs=
                                                      {'class': 'form-control','name':'LastName', 'placeholder':
                                                          "نام خانوادگی خود را وارد کنید"}))
    email = forms.EmailField(label='', max_length=50,
                             widget=forms.TextInput(attrs=
                                                    {'class': 'form-control','name':'Email' ,'placeholder':
                                                        'ایمیل خود را وارد کنید'}))
    username = forms.CharField(label='', max_length=50,
                               widget=forms.TextInput(attrs=
                                                      {'class': 'form-control','name':'username', 'placeholder':
                                                          'نام کابری خود را وارد کنید'}))
    password1 = forms.CharField(label='', max_length=50, widget=forms.PasswordInput(attrs=
                                                                                    {"class": 'form-control',
                                                                                     'name': 'password',
                                                                                     "type": "password",
                                                                                     'placeholder': "رمز خود را وارد کنید"}))
    password2 = forms.CharField(label='', max_length=50, widget=forms.PasswordInput(attrs=
                                                                                    {"class": 'form-control',
                                                                                     'name': 'password',
                                                                                     "type": "password",
                                                                                     'placeholder': "دوباره رمز خود را وارد کنید"}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class UpdateUser(UserChangeForm):
    password = None
    first_name = forms.CharField(label='', max_length=50,
                                widget=forms.TextInput(attrs=
                                                       {'class': 'form-control','name': 'FirstName',
                                                        'placeholder': 'نام خود را وارد کنید'}))
    last_name = forms.CharField(label='', max_length=50,
                               widget=forms.TextInput(attrs=
                                                      {'class': 'form-control','name':'LastName', 'placeholder':
                                                          "نام خانوادگی خود را وارد کنید"}))
    email = forms.EmailField(label='', max_length=50,
                             widget=forms.TextInput(attrs=
                                                    {'class': 'form-control','name':'Email' ,'placeholder':
                                                        'ایمیل خود را وارد کنید'}))
    username = forms.CharField(label='', max_length=50,
                               widget=forms.TextInput(attrs=
                                                      {'class': 'form-control','name':'username', 'placeholder':
                                                          'نام کابری خود را وارد کنید'}))



    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


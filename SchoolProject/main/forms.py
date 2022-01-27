from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *

common_class = "u-border-1 u-border-grey-30 u-input u-input-rectangle u-white"

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': common_class,
                                                                            'placeholder': "Логин"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': common_class,
                                                                                  'placeholder': "Пароль"}))
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput(attrs={'class': common_class,
                                                                                            'placeholder': "Повтор пароля"}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': common_class,
                                                                            'placeholder': "Логин"}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': common_class,
                                                                                 'placeholder': "Пароль"}))

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label="Старый пароль", widget=forms.PasswordInput(attrs={'class': common_class,
                                                                                         'placeholder': "Старый пароль"}))
    new_password1 = forms.CharField(label="Новый пароль", widget=forms.PasswordInput(attrs={'class': common_class,
                                                                                        'placeholder': "Новый пароль"}))
    new_password2 = forms.CharField(label="Подтверждение нового пароля", widget=forms.PasswordInput(attrs={'class': common_class,
                                                                                                       'placeholder': "Повтор нового пароля"}))
    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

class ChangeUserDataForm(UserChangeForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': common_class,
                                                                            'placeholder': "Введите логин"}))
    first_name = forms.CharField(label="Имя", required=False, widget=forms.TextInput(attrs={'class': common_class,
                                                                                            'placeholder': "Введите имя"}))
    last_name = forms.CharField(label="Фамилия", required=False, widget=forms.TextInput(attrs={'class': common_class,
                                                                                               'placeholder': "Введите фамилию"}))
    email = forms.EmailField(label="Электронная почта", required=False, widget=forms.EmailInput(attrs={'class': common_class,
                                                                                                       'placeholder': "Введите электронную почту"}))
    password = None
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
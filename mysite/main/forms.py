from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import TextInput, PasswordInput, CharField


class RegisterUserForm(UserCreationForm):
    username = CharField(label='Имя пользователя',
                         widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = CharField(label='Подтвердите пароль',
                          widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = CharField(label='Имя пользователя',
                         widget=TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя пользователя'}))
    password = CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

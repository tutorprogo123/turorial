from django import forms
from .models import Accounts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AccountsForm(forms.ModelForm):
  class Meta:
    model = Accounts
    fields = ["title", "username", "password"]
    labels = {
        "title": "サイト名",
        "username": "ユーザー名(またはメールアドレス)",
        "password": "パスワード",
    }


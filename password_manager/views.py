from django.shortcuts import render, redirect
from .models import Accounts
from .forms import AccountsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 


# Create your views here.

@login_required(login_url="login")
def top(request):
  # passwords = [
  #   {
  #     "title": "google",
  #     "username": "whyskyblue",
  #     "password": "12345678",
  #   },
  #   {
  #     "title": "yahoo",
  #     "username": "whyoceanblue",
  #     "password": "87654321",
  #   },
  # ]

  accounts = Accounts.objects.all()

  return render(request, 'password_manager/top.html', {
    "accounts": accounts
  })


@login_required(login_url="login")
def add(request):
  if request.method == "GET":
    form = AccountsForm()
    return render(request, "password_manager/add.html", {
    "form": form
    })

  elif request.method == "POST":
    form = AccountsForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect("top")


@login_required(login_url="login")
def update(request, id):
  account = Accounts.objects.get(id=id)
  form = AccountsForm(instance=account)

  if request.method == "POST":
    form = AccountsForm(request.POST, instance=account)
    if form.is_valid():
      form.save()
      return redirect("top")

  return render(request, "password_manager/update.html", {
    "form": form,
    "account": account,
  })


@login_required(login_url="login")
def delete(request, id):
  account = Accounts.objects.get(id=id)

  if request.method == "POST":
    account.delete()
    return redirect("top")
  
  return render(request, "password_manager/delete.html", {
    "account": account,
  })


def loginPage(request):
  if request.user.is_authenticated:
    return redirect("top")
  else:
    if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect("top")
      else:
        messages.info(request, "ユーザー名かパスワードが間違えています")
    return render(request, "password_manager/login.html")


def logoutUser(request):
  logout(request)
  return redirect("login")
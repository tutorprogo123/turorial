from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.top, name='top'),
  path("add/", views.add, name="add"),
  path("update/<int:id>", views.update, name="update"),
  path("delete/<int:id>", views.delete, name="delete"),

  path("login/", views.loginPage, name="login"),
  path("logout", views.logoutUser, name="logout"),
]

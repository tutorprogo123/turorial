from django.db import models

# Create your models here.
class Accounts(models.Model):
  title = models.CharField(max_length=50)
  username = models.CharField(max_length=50, )
  password = models.CharField(max_length=50, )

  class Meta:
    verbose_name_plural = 'アカウント'

  def __str__(self):
    return self.title
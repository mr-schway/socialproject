from django.conf import settings
from django.db import models

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  photo = models.ImageField(upload_to='users/%Y/%m/$d', blank=True)

  def __str__(self):
    return self.user.username
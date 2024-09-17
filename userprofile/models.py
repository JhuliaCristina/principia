from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    username = models.CharField(max_length=40, null = True)
    password = models.CharField(max_length=40, null = True)
    user = models.OneToOneField(User, related_name= 'userprofile', on_delete= models.CASCADE) #deletando todos os dados do usuário 

    def __Str__(self):
        return self.user.username
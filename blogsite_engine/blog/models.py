from django.db import models


class User (models.Model):
    username = models.CharField(max_length=200)
    user_login = models.CharField(max_length=200)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['username', ]
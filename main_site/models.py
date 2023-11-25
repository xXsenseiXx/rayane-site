from django.db import models

# Create your models here.


class user(models.Model):
    sess = models.TextField()

    def __str__(self):
        return self.sess
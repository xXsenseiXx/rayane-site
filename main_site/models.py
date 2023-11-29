from django.db import models

# Create your models here.


class user(models.Model):
    sess = models.TextField()

    def __str__(self):
        return self.sess
    

class product(models.Model):

    user = models.ForeignKey("user", on_delete=models.CASCADE)

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=5,decimal_places=2)

    image = models.ImageField(upload_to='images/', blank=False, null=False)

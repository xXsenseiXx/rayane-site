from django.db import models

# Create your models here.


class user(models.Model):
    sess = models.TextField()

    def __str__(self):
        return self.sess
    

class product(models.Model):

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=5,decimal_places=2)

    image = models.ImageField(upload_to='images/', blank=False, null=False)

class watchlist(models.Model):

    client = models.ForeignKey(user, on_delete=models.CASCADE, related_name="user_watchlist")

    item = models.ForeignKey(product, on_delete=models.CASCADE)
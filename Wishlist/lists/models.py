from django.db import models
from django.contrib.postgres.fields import ArrayField

class Wishlist(models.Model):
    class wlstuct():
        text=models.CharField(max_length=200)
        compl=models.BooleanField(default=False)
        #gifter=models.ForeignKey(User, editable=False)
    wishlist=ArrayField(wlstuct, blank=True)
    #user=models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    #friends=models.ManyToManyField(User, default={'admin'}, null = True)
    def __str__(self):
        return self.title
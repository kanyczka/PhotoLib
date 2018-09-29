from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=64)

    class Meta:
        ordering = ['username']

    def __str__(self):
        return self.username

class Photo(models.Model):
    path = models.ImageField(max_length=128, upload_to="photos/", verbose_name="zdjęcie")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="data dodania")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

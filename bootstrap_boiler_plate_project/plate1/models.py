from django.db import models


class Ask(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
    useremail = models.EmailField(max_length=128)
    username = models.CharField(max_length=32)
    upload_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title  
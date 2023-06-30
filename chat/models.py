from django.db import models


class Messages(models.Model):
    room_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    content = models.TextField(max_length=500)


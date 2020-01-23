from django.db import models

class Last_User(models.Model):
    ip = models.CharField(max_length = 32)

    def __str__(self):
        return self.ip
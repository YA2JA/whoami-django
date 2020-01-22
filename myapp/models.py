from django.db import models

class Last_Users(models.Model):
    IP = models.CharField(max_length = 15)

    def __str__(self):
        return self.IP
    
from django.db import models


# Create your models here.
class Registered_email(models.Model):
    """
    Prevent Duplicate Email
    """

    email = models.CharField(max_length=40)

    def __str__(self):
        return self.email

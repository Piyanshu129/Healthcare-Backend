from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom user based on AbstractUser but with unique email and name field.
    We'll still keep username to satisfy AbstractUser internals.
    Login will be via email in our serializers / token view.
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # username still required by AbstractUser

    def __str__(self):
        return self.email

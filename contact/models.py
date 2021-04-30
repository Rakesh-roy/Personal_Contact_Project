from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ContactModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=100, null=True, blank=True)
    CHOISE = (
        ("Friends","Friends"),
        ("Family","Family"),
        ("Office","Office"),
        ("Faculty","Faculty"),
    )
    category = models.CharField(max_length=100, choices=CHOISE)

    def __str__(self):
        return self.name


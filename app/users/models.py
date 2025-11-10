from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')],
        blank=True
    )
    height_cm = models.FloatField(null=True, blank=True)
    weight_kg = models.FloatField(null=True, blank=True)
    goal = models.CharField(
        max_length=50,
        choices=[
            ('Weight Loss', 'Weight Loss'),
            ('Muscle Gain', 'Muscle Gain'),
            ('Maintenance', 'Maintenance')
        ],
        blank=True
    )

    def __str__(self):
        return self.username

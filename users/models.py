
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('buyer', 'Buyer'),
        ('seller', 'Seller'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_verified = models.BooleanField(default=True)  # simplify for demo (enable email later)
    profile_image = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    about_me = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username


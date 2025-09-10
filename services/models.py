
from django.db import models
from users.models import User

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('graphic_design', 'Graphic Design'),
        ('writing', 'Writing'),
        ('programming', 'Programming'),
    ]
    seller = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'seller'})
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    delivery_time = models.IntegerField(help_text='Delivery time in days')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reviews')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'buyer'})
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.service.title} - {self.rating}/5"

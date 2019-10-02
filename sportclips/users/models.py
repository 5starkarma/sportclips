from PIL import Image
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    EMPLOYEE_CHOICES = (
        ('stylist', 'STYLIST'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    employee_type = models.CharField(
        max_length=30, choices=EMPLOYEE_CHOICES, default='dealer')


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

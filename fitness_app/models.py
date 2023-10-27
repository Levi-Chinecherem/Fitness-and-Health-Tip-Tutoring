# fitness_app/models.py
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class UserProfile(models.Model):
    MALE = 'Male'
    FEMALE = 'Female'

    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100, choices=SEX_CHOICES)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.full_name} - {self.user.username}"
    
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'Users Profile'

class FitnessTip(models.Model):
    title = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='designs/cover_images/')
    content = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fitness_tips')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Fitness Tip'
        verbose_name_plural = 'Fitness Tips'

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    """

    class GenderChoices(models.TextChoices):
        MASCULINE = 'Masculine', 'Masculine'
        FEMININE = 'Feminine', 'Feminine'
        OTHER = 'Other', 'Other'

    description = models.TextField(blank=True, null=True, max_length=500)
    gender = models.CharField(choices=GenderChoices.choices, max_length=10, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.username

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        return super().get_full_name() or self.username


class DrawingPage(models.Model):
    """
    Model representing a page that contains multiple drawings.
    """
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, related_name='drawing_pages', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'drawing page'
        verbose_name_plural = 'drawing pages'

    def __str__(self):
        return self.title


class Drawing(models.Model):
    """
    Model representing a drawing uploaded by a user.
    """
    image = models.ImageField(upload_to='drawings/')
    drawing_page = models.ForeignKey(DrawingPage, related_name='drawings', on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'drawing'
        verbose_name_plural = 'drawings'

    def __str__(self):
        return f'Drawing by {self.user.username} uploaded at {self.uploaded_at}'

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Profile(models.Model):

    LANGUAGES = (
        ('EN', 'EN'),
        ('FR', 'FR')
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(
        max_length=255, null=True, blank=True, help_text='user phone number')
    dob = models.DateField(_("Date of birth"),null=True, blank=True,
                           help_text='user date of birth')
    city = models.CharField(max_length=255, blank=True,
                            null=True, help_text='user\'s city ')
    lang = models.CharField(max_length=2, choices=LANGUAGES,
                            default='EN', help_text='user language')
    created_at = models.DateTimeField(default=timezone.now)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.user.username}'

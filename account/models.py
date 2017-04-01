from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

    email_hashtag = models.CharField(max_length=256)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.email_hashtag = default_token_generator.make_token(self.user)

        super().save(*args, **kwargs)

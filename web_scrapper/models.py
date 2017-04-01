import datetime
from django.db import models

# Create your models here.
from django.utils import timezone

from account.models import Profile


class Hashtag(models.Model):
    name = models.CharField(max_length=256, unique=True)


class Link(models):
    url = models.URLField()
    comment = models.CharField(max_length=256, blank=True, null=True, default="")
    search_profile_result = models.ForeignKey(SearchProfileResults, related_name="links", on_delete=models.CASCADE)


class SearchProfileResults(models.Model):
    updated = models.DateTimeField(auto_now=True)


class SearchProfile(models.Model):
    RANGE_CHOICES = (
        ('title', 'Title'),
        ('text', 'Text'),
        ('title_and_text', 'Title and text'),
    )

    profile = models.ForeignKey(Profile, related_name='search_profiles')
    hashtags = models.ManyToManyField(Hashtag, related_name='search_profiles')
    range = models.CharField(max_length=50, choices=RANGE_CHOICES, default=RANGE_CHOICES[3][0])
    date_from = models.DateTimeField()
    date_to = models.DateTimeField(default=timezone.now)
    result = models.OneToOneField(SearchProfileResults, related_name='search_profile', on_delete=models.SET_NULL,
                                  null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.date_from:
            self.date_from = timezone.now() - datetime.timedelta(days=30)
        super().save(*args, **kwargs)

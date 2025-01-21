# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    years_of_experience = models.IntegerField(null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Topic(models.Model):

    #__Topic_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Topic_FIELDS__END

    class Meta:
        verbose_name        = _("Topic")
        verbose_name_plural = _("Topic")


class Newspaper(models.Model):

    #__Newspaper_FIELDS__
    content = models.TextField(max_length=255, null=True, blank=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    #__Newspaper_FIELDS__END

    class Meta:
        verbose_name        = _("Newspaper")
        verbose_name_plural = _("Newspaper")



#__MODELS__END

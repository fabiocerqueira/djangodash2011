# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Event(models.Model):
    admin = models.ForeignKey(User)
    name = models.CharField(max_length=80)
    slug = models.SlugField(max_length=80)
    description = models.TextField()
    event_start = models.DateTimeField()
    event_end = models.DateTimeField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    hashtag = models.CharField(max_length=255, blank=True, help_text=_("hashtag separated by commas"))

    def __unicode__(self):
        return self.name


class Presentation(models.Model):
    event = models.ForeignKey(Event)
    title = models.CharField(max_length=100)
    speaker = models.CharField(max_length=120)
    description = models.TextField()
    slides = models.URLField(verify_exists=False, blank=True)
    video = models.URLField(verify_exists=False, blank=True)

    def __unicode__(self):
        return u"%s - %s - %s" % (self.event.name, self.title, self.speaker)

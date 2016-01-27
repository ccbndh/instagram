from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.contrib.auth.models import User


@python_2_unicode_compatible  # only if you need to support Python 2
class Photo(models.Model):
    user = models.ForeignKey(User, related_name="uploader")
    title = models.CharField(max_length=120, blank=True, null=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

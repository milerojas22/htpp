from __future__ import unicode_literals

from django.db import models


class PersonMonoku(models.Model):
    name_person = models.CharField(max_length=255)
    email_person = models.EmailField(max_length=255)
    age_person = models.IntegerField(max_length=255)

# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Purchase(models.Model):
    caption = models.CharField(u"שם הרכישה", max_length=120)
    description = models.TextField(u'תאור הרכישה', blank=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('Category', null=True, unique=False)
    time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.caption

    
class Category(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

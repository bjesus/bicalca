# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Need(models.Model):
    caption = models.CharField(u"שם המוצר", max_length=120)
    description = models.TextField(u'תאור המוצר')
    bought = models.BooleanField(default=False)
    bought_by = models.ForeignKey(User, null=True, related_name="buys", unique=False)
    user = models.ForeignKey(User, related_name="needs", unique=False)
    
    def __unicode__(self):
        return self.caption

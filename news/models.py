# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    url = models.CharField(max_length=255, unique=True, default="")
    def __unicode__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    def __unicode__(self):
	    return self.name

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255,default="")
    url = models.CharField(max_length=255, unique=True, default="")
    pub_date = models.DateTimeField('date published',null=True)
    category = models.ForeignKey(Category,null=True,blank=True)
    tag = models.ManyToManyField(Tag, related_name="tag",blank=True)
    def __unicode__(self):
		return self.title

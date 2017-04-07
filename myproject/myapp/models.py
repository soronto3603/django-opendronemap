# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%d')
    project_name = models.CharField(max_length=200)
    status = models.CharField(max_length=10)

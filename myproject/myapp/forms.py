# -*- coding: utf-8 -*-

from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='Select a file')
    project_name = forms.CharField(max_length=200)

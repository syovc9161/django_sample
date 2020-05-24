from __future__ import unicode_literals
from django import forms
from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        # fields = ('image', 'content', )
        exclude = ('filtered_image', )

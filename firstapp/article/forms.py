#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'nikitachukov'
from django.forms import ModelForm
from models import Comments

class CommentForm(ModelForm):
    class Meta:
        model=Comments
        fields = ['comments_text']
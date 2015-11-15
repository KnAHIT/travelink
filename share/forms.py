# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:49:12 2015

@author: Kevinyyyx
"""

from django import forms
from models import Blog,Account

class BlogForm(forms.ModelForm):
    class Meta:    
        model = Blog
        fields = "__all__"
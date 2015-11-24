# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 15:49:12 2015

@author: Kevinyyyx
"""

from django import forms
from models import Blog,Account,Travel_plan,Diary

class BlogForm(forms.ModelForm):
    class Meta:    
        model = Blog
        fields = "__all__"
        
class TravelPlanForm(forms.ModelForm):
    class Meta:
        model = Travel_plan
        fields = "__all__"
        
class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ['Title','Passage','Tag','Image']
        
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
    password = forms.CharField(label='password',widget=forms.PasswordInput())

class PlanForm(forms.ModelForm):
    class Meta:
        model = Travel_plan
        fields = ['Start_date','End_date','People_amount','Budget','Demand']

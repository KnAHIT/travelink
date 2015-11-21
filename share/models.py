from django.db import models

# Create your models here.
#from django.contrib.auth.models import User

class Account(models.Model):    
    Username = models.CharField(max_length=20)
    Email = models.EmailField(max_length=254, blank=True)
    Image = models.ImageField(upload_to = './upload/headimage/',blank=True)
    def __unicode__(self) :
        return self.Username
        
class Blog(models.Model):
    Username = models.ForeignKey(Account)    
    Title = models.CharField(max_length=20,blank = True, null = True)
    Passage = models.TextField(blank = True, null = True)
    Tag = models.CharField(max_length = 50,blank = True,null=True)
    Date_time = models.DateTimeField(auto_now_add = True)   
    Image = models.ImageField(upload_to = './upload/',blank = True,null=True)
        
    def __unicode__(self) :
        return self.Title

    class Meta:  
        ordering = ['-Date_time']
    
class Travel_plan(models.Model):
        Username = models.ForeignKey(Account)          
        Destination = models.CharField(max_length=20)
        Start_place = models.CharField(max_length=20)
        Start_date = models.DateField()
        End_date = models.DateField()
        People_amount = models.IntegerField()
        Budget = models.IntegerField() 
        Demand = models.CharField(max_length = 100,blank=True)        
        
        def __unicode__(self) :
            return self.Destination
    
class Diary(models.Model):
    Username = models.ForeignKey(Account)
    Title = models.CharField(max_length=20,blank = True, null = True)
    Passage = models.TextField(blank = True, null = True)
    Tag = models.CharField(max_length = 50, blank = True,null=True)
    Date_time = models.DateTimeField(auto_now_add = True)   
    Image = models.ImageField(upload_to = './upload/diary/',blank=True,null=True)
    Destination = models.CharField(max_length=20)
    
    def __unicode__(self) :
        return self.Title

    class Meta:  
        ordering = ['-Date_time']    
    
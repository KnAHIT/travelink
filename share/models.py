from django.db import models

# Create your models here.
#from django.contrib.auth.models import User

class Account(models.Model):    
    Username = models.CharField(max_length=20)
    Email = models.EmailField(max_length=254, blank=True)
    Travel_plan = models.CharField(max_length=200)
    def __unicode__(self) :
        return self.Username
class Blog(models.Model):
    Username = models.ForeignKey(Account)    
    Title = models.CharField(max_length=20)
    Passage = models.TextField(blank = True, null = True)
    Tag = models.CharField(max_length = 50, blank = True)
    Date_time = models.DateTimeField(auto_now_add = True)   
    Image = models.ImageField(upload_to = './upload/',blank=True)
        
    
    def __unicode__(self) :
        return self.Title

    class Meta:  
        ordering = ['-Date_time']
    
    
    
    
    
    
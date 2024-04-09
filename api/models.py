from django.db import models
 
class Job(models.Model):
    date_in = models.CharField(max_length=200)
    date_out = models.CharField(max_length=200)
    organisation = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField(default=None)
    def __str__(self):
        return self.organisation
    
    
class Bio(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    about_me = models.TextField(default=None)
    def __str__(self):
        return self.name 

class Skills(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

    
class Projects(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default=None)
    url = models.CharField(max_length=200)
    def __str__(self):
        return self.name    



# class audiens
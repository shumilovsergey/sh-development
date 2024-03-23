from django.db import models
 
class Job(models.Model):
    organisation = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    description = models.TextField(default=None)

    def __str__(self):
        return self.organisation
    
class Career(models.Model):
    date_in = models.CharField(max_length=20)
    date_out = models.CharField(max_length=20)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return self.job.organisation
    
class Bio(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    about_me = models.TextField(default=None)

    def __str__(self):
        return self.name 

class Skills(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=20)
    value = models.CharField(max_length=20)
    def __str__(self):
        return self.name 
    
class Projects(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(default=None)
    url = models.CharField(max_length=200)
    def __str__(self):
        return self.name    



# class audiens

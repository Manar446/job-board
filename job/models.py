from django.db import models

# Create your models here.
JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Job(models.Model): # column
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=20, choices=JOB_TYPE)
    desciption = models.TextField(max_length=1000)
    published_on = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE) # it comes after this is why single qouts
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
        
    
    
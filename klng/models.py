from django.db import models

# Create your models here.

class User(models.Model): 
    email = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name

class Portfolio(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolio', null=True)
    name = models.CharField(max_length=100, default='No name')
    about = models.CharField(max_length=400, default='No info about me')
    github_link = models.CharField(max_length=200, null=True)
    linkedin_link = models.CharField(max_length=200, null=True)
    image_url = models.CharField(max_length=200, null=True)
        
    def __str__(self):
        return self.name


class Project(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='project')
    project_name = models.CharField(max_length=100, default='no project name')
    desc = models.CharField(max_length=400, default='no description')
    project_link = models.CharField(max_length=200, null=True)
    image_url = models.CharField(max_length=200, null=True)
    
        
    def __str__(self):
        return self.project_name


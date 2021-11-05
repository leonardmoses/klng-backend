# Register your models here.
from django.contrib import admin
from .models import User, Portfolio, Project

admin.site.register(User)
admin.site.register(Portfolio)
admin.site.register(Project)
from django.contrib import admin
from .models import Message, PastProject, FutureProject
# Register your models here.
admin.site.register(Message)
admin.site.register(PastProject)
admin.site.register(FutureProject)
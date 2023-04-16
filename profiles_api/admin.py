from django.contrib import admin
from profiles_api import models


# Register your models here.
admin.site.register(models.UserProfile) # It is used to make userprofile model accessible form admin interface
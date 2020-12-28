from django.contrib import admin
from appnew.models import *
from .models import UserProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Category)
admin.site.register(Product)

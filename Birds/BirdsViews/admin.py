from django.contrib import admin
from .models import User, Birds, ViewedUser


admin.site.register(User)
admin.site.register(Birds)
admin.site.register(ViewedUser)

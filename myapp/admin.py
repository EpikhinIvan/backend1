from django.contrib import admin
from .models import UserProfile, Application

# Регистрация моделей
admin.site.register(UserProfile)
admin.site.register(Application)

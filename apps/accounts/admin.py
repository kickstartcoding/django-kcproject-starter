from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.accounts.models import User

# Register custom User class using the UserAdmin
admin.site.register(User, UserAdmin)

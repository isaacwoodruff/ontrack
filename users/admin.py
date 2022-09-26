from django.contrib import admin
from users.models import Profile

@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'github')

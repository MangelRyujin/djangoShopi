from django.contrib import admin

from apps.accounts.models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','phone_number','country','city','address']
from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ['name','phone_number','password','create_date']

admin.site.register(User,UserAdmin)


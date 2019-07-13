from django.contrib import admin

from .models import User, DropUser


class UserAdmin(admin.ModelAdmin):
    list_display = [
        '__str__', 'name', 'nickname', 'phone_number',
        'gender',
    ]

admin.site.register(User, UserAdmin)
admin.site.register(DropUser)

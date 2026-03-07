from django.contrib import admin
from .models import User

class AdminUser(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'email', )
    list_filter = ('email',)
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, AdminUser)
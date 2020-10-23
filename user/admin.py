from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username','name', 'email', 'is_staff', 'is_active',)
    list_filter = ('username','name', 'email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username','name', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','name', 'password1', 'password2', 'is_staff', 'is_active')}),
    )
    search_fields = ('username',)
    ordering = ('username',)

### register custom user model to admin
admin.site.register(CustomUser, CustomUserAdmin)
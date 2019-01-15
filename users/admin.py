from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = [
        'last_name',
        'first_name',
        'email',
        'net_id',
        'phone_number',
        'supervisor',
        'institution',
        'cost_center',
        'cost_center_end_date',
        'last_login',
        'date_joined',
    ]
    list_display_links = ['last_name', 'first_name', 'email']
    readonly_fields = ['last_login', 'date_joined']
    fieldsets = (
        (None, {'fields': ('email', 'net_id')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'phone_number',)}),
        ('Accounting Info', {'fields': ('supervisor', 'institution', 'cost_center', 'cost_center_end_date',)}),
        ('Forms', {'fields': ('activation_form', 'training_form',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email','is_staff','is_active','last_login']
    ordering = ['email']
    fieldsets = (
        (None, {'fields':('email','password')}),
        ('Permissions',{'fields':('is_staff','is_active','is_superuser')})
    )

    add_fieldsets = (
        (None,
         {
             'classes' : ('wide'),
             'fields' : ('email','password1','password2','is_staff','is_active')
         })
    )

    search_fields = ('email',)

admin.site.register(User,CustomUserAdmin)
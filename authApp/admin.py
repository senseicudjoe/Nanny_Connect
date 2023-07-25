from django.contrib import admin
from .models import Customuser
from django.contrib.auth.admin import UserAdmin




# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = Customuser()
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Fields', 
            {'fields':
                (
                    'is_nurse',
                    'is_client',
                    'is_admin',
                )
            }
        ),
    )
    
admin.site.register(Customuser, CustomUserAdmin)

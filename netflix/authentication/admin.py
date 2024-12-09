from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'birth_date')
    search_fields = ('user__username', 'user__email')  # Buscar por nombre o email del usuario

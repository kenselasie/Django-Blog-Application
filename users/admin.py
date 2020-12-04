from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users



class MyUserAdmin(UserAdmin):
    list_display = ('email', 'id', 'firstname', 'username', 'date_joined', 'last_login', 'is_admin') # Whats going to be displayed as headers in the admin
    search_fields = ('email', 'username')
    readonly_fields = ('email', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    add_fieldsets = (
        (None, {
        'classes': ('wide',),
        'fields': ('firstname', 'lastname', 'othernames', 'email', 'username', 'phone_num', 'is_superuser', 'password1', 'password2')}   # here are fields you want to have in django-admin AddUser view
        ),
    )
admin.site.register(Users, MyUserAdmin)
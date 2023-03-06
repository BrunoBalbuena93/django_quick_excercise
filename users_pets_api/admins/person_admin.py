from django.contrib import admin


class PersonAdmin(admin.ModelAdmin):

    list_display = ['username', 'first_name', 'last_name', 'phone_number', 'city', 'last_login']
    search_fields = ['username', 'first_name', 'last_name', 'phone_number', 'city', 'last_login']
    list_filter = ['username', 'first_name', 'last_name', 'phone_number', 'city', 'last_login']
    ordering = ['username', 'first_name', 'last_name', 'phone_number', 'city', 'last_login']

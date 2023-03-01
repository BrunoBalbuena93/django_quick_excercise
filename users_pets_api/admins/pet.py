from django.contrib import admin


class PetAdmin(admin.ModelAdmin):

    list_display = ['date_of_birth', 'deceased_date', 'breed', 'gender', 'weight', 'id']
    search_fields = ['date_of_birth', 'deceased_date', 'breed', 'gender', 'weight', 'id']
    list_filter = ['date_of_birth', 'deceased_date', 'breed', 'gender', 'weight', 'id']
    ordering = ['date_of_birth', 'deceased_date', 'breed', 'gender', 'weight', 'id']

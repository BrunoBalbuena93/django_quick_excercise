from django.contrib import admin


class OwnerAdmin(admin.ModelAdmin):

    list_display = ["person", "pet"]
    search_fields = ["person", "pet"]
    list_filter = ["person", "pet"]
    ordering = ["person", "pet"]

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import Drawing, DrawingPage, User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {
            "fields": ("gender", "description", "profile_image"),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {
            "fields": ("gender", "description", "profile_image"),
        }),
    )
    list_display = UserAdmin.list_display + ("gender",)
    search_fields = UserAdmin.search_fields + ("gender",)



@admin.register(DrawingPage)
class DrawingPageAdmin(admin.ModelAdmin):
    pass



@admin.register(Drawing)
class DrawingAdmin(admin.ModelAdmin):
    pass

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin

# # from .forms import CustomUserCreationForm, CustomUserChangeForm
# from .models import Users,Groups


# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = Users
#     list_display = ("email", "is_staff")
#     list_filter = ("email", "is_staff")
#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         ("Permissions", {"fields": ("user_permissions", "is_staff")}),
#     )
#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": (
#                 "email", "password1", "password2", "user_permissions", "is_staff"
#             )}
#         ),
#     )
#     search_fields = ("email",)
#     ordering = ("email",)


# admin.site.register(Users, CustomUserAdmin)
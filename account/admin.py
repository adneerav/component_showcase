from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from account.forms import UserAdminCreationForm, UserAdminChangeForm
from account.models import User, Profile


class UserProfile(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    list_display = ['full_name', 'nick_name']


class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    inlines = (UserProfile,)

    list_display = ('email', 'username', 'full_name', 'admin', 'active')
    list_filter = ('admin', 'active')
    list_display_links = ('username', 'email')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('admin', 'staff', 'active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'email', 'username', 'password', 'confirm_password')}
         ),
    )
    search_fields = ('email', 'full_name',)
    ordering = ('email', 'username')
    filter_horizontal = ()

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, UserAdmin)

# admin.site.register(Profile, UserProfile)
# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

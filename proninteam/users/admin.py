from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _
from users.models import Role, User


class UserCreationForm(forms.ModelForm):
    """Form for creating a new user using admin panel."""
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email', )

    def clean_password2(self):
        """Password validation."""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        """Save password."""
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """Form for change user password using admin panel."""
    password = ReadOnlyPasswordHashField(
        label="Password",
        help_text=_(
            'У вас нет возможности посмотреть захешированный пароль, '
            'но вы можете изменить его, используя '
            '<a href=\"../password/\">эту форму</a>.'
        )
    )

    class Meta:
        model = User
        fields = ('email', )

    def clean_password(self):
        return self.initial['password']


class UserAdmin(BaseUserAdmin):
    """
    User admin panel.
    With custom filter params.
    """

    form = UserChangeForm
    add_form = UserCreationForm

    list_display = (
        'email',
    )
    list_filter = (
        'is_superuser',
        'main_role',
    )
    fieldsets = (('Personal info', {
        'fields': (
            'email',
            'phone',
            'first_name',
            'middle_name',
            'last_name',
            'main_role',
            'other_roles',
            'photo',
            'is_staff',
            'is_active',
            'password',
        )
    }),)
    add_fieldsets = ((None, {
        'classes': ('wide',),
        'fields': (
            'email',
            'phone',
            'first_name',
            'middle_name',
            'last_name',
            'main_role',
            'other_roles',
            'photo',
            'is_staff',
            'is_active',
            'password1',
            'password2',
        )
    }),)
    search_fields = (
        'email',
    )
    ordering = ('-email',)
    filter_horizontal = ()


admin.site.unregister(Group)
admin.site.register(Role)
admin.site.register(User, UserAdmin)

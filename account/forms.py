from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from account.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_email(self):
        email = self.cleaned_data.get('email', )
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username', )
        if username is None:
            raise forms.ValidationError("Username required")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Already exist this username.")
        return username

    def clean_confirm_password(self):
        # Check that the two password entries match
        password = self.cleaned_data.get("password", )
        confirm_password = self.cleaned_data.get("confirm_password", )
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password


class UserAdminCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'username', 'password', 'full_name')

    def clean_username(self):
        username = self.cleaned_data.get('username', )
        if username is None:
            raise forms.ValidationError("Username required")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Already exist this username.")
        return username

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password', )
        confirm_password = self.cleaned_data.get('confirm_password', )
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Password & Confirm Password does not match.")
        return confirm_password

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name", )
        if not full_name:
            raise forms.ValidationError("Full Name required.")
        return full_name

    def save(self, commit=True):
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.staff = True
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    full_name = forms.CharField(label='Full name', widget=forms.TextInput)

    class Meta:
        model = User
        fields = ('email', 'password', 'active', 'admin', 'full_name')

    def clean_full_name(self):
        full_name = self.cleaned_data.get("full_name", )
        if not full_name:
            raise forms.ValidationError("Full name required.")
        return full_name

    def clean_password(self):
        return self.initial["password"]

    def save(self, commit=True):
        user = super(UserAdminChangeForm, self).save(commit=False)
        if commit:
            user.save()
        return user

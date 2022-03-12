
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from account.models import User

# class CustomUserCreationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=255, required=True)
#     last_name = forms.CharField(max_length=255, required=True)
#     email = forms.EmailField(required=True)
#     phone = forms.CharField(min_length=10, max_length=10, required=True)
    
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')
        
#     def save(self, commit=True):
#         user = super(CustomUserCreationForm, self).save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#         user.phone = self.cleaned_data['phone']
#         if commit:
#             user.save()
#         return user

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone',)

class CustomUserCreationForm(forms.ModelForm):
    first_name = forms.CharField(
    max_length=25, help_text='Required', label='First-Name')
    last_name = forms.CharField(
    max_length=25, help_text='Required', label='Last-Name')
    email = forms.EmailField(
    max_length=50, label='Email', help_text='Required')
    phone = forms.CharField(
        min_length=10, max_length=10, help_text='Required', label='Phone-number')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        widget=forms.PasswordInput, label='Confirm-Password')

    def __init__(self, *args, **kwargs):
        '''another way to style form elements'''

        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({
            'placeHolder': 'First name',
            'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['last_name'].widget.attrs.update({
            'placeHolder': 'Last name',
            'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['email'].widget.attrs.update({
            'placeHolder': 'Email-address',
            'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['phone'].widget.attrs.update({
            'placeHolder': 'Phone-number',
            'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['password'].widget.attrs.update({
            'placeHolder': 'Password',
            'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })
        self.fields['confirm_password'].widget.attrs.update({
            'placeHolder': 'Confirm-Password',
            'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-700 focus:ring-opacity-50 rounded-md'
        })

    class Meta:
        model = User
        fields = ('phone', 'email', 'first_name')

    def clean(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        phone = cleaned_data.get('phone')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # check if username exist
        user = User.objects.filter(phone=phone)
        if user:
            raise forms.ValidationError(
                "That Phone-number is already taken , please select another ")
        # check if email exist
        email = User.objects.filter(email=email)
        if email:
            raise forms.ValidationError(
                "That email is already taken , please select another ")
        # check password
        if password != confirm_password:
            raise forms.ValidationError(
                "Your password and confirm password do not match!")

        return cleaned_data
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Phone Number',
        'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-600 focus:ring-opacity-50 rounded-md'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'block w-full px-4 py-2 mt-2 text-md placeholder-gray-400 focus:outline-none border border-blue-500 focus:ring-1 focus:ring-blue-600 focus:ring-opacity-50 rounded-md'
    }))
    
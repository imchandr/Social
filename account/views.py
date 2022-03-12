from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import HttpResponseRedirect
import random
from account.forms import CustomUserCreationForm


def home_page(request):
    return render(request, 'account/landing_page.html')

def register(request):
    if request.method == 'POST':
        registerForm = CustomUserCreationForm(request.POST)
        
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            
            user = registerForm.save(commit=False)
            user.first_name = registerForm.cleaned_data['first_name']
            user.last_name = registerForm.cleaned_data['last_name']
            user.email = registerForm.cleaned_data['email']
            user.phone = registerForm.cleaned_data['phone']
            user.username = registerForm.cleaned_data['phone']
            user.set_password(registerForm.cleaned_data['password'])
            user.save()
            return redirect('/account/login')
            
			
            
        else:
            registerForm.errors
            
    else:
        registerForm = CustomUserCreationForm()
    
    return render(request, 'account/register.html', {'form':registerForm})
        
            





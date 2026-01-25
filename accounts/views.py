from django.shortcuts import render
from accounts.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
    form = RegistrationForm()
    context_dict = {
        'form':form
    }
    return render(request, 'register.html',context_dict)
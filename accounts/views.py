from django.shortcuts import render
from accounts.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User

# Create your views here.

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            if(form.cleaned_data['password'] != form.cleaned_data['confirm_password']):
                form.add_error('confirm_password', 'Passwords do not match')
                print("error",form.errors)
                context_dict = {
                    'form':form
                }
                return render(request, 'register.html',context_dict)

            else:
                user = User.objects.create_user(
                    username = form.cleaned_data['username'],
                    email = form.cleaned_data['email'],
                    password=form.cleaned_data['password']
                )
                user.save()

        else:
            print("form is not valid", form.errors)

    form = RegistrationForm()
    context_dict = {
        'form':form
    }
    return render(request, 'register.html',context_dict)
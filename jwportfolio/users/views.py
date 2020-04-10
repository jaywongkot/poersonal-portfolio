from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST': # We check wether the request from user is a POST request or GET request.
        form = UserRegisterForm(request.POST) # I want to create a new form that come with a POST request data.
        if form.is_valid(): # Then django will check, wether the new data from a registration form valid or not,
            form.save() # It will the user after our form validated
            username = form.cleaned_data.get('username') # if it is valid then create a new username with a new account,
                                                        # if it's not valid then jump to else condition.
            messages.success(request, f'Account created for {username}!') # f'' call f string and it is available on python 3.6 up
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form}) # Here it will render a form with a new username filled in that filed

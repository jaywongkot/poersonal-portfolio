from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    # We check wether the request from user is a POST request or GET request.
    if request.method == 'POST':
        # I want to create a new form that come with a POST request data.
        form = UserRegisterForm(request.POST)
        if form.is_valid():  # Then django will check, wether the new data from a registration form valid or not,
            form.save()  # It will the user after our form validated
            # if it is valid then create a new username with a new account, if it's not valid then jump to else condition.
            username = form.cleaned_data.get('username')
            # f'' call f string and it is available on python 3.6 up
            messages.success(
                request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    # Here it will render a form with a new username filled in that filed
    return render(request, 'users/register.html', {'form': form})


@login_required  # Setting a user must login to view the specific url
def profile(request):
    return render(request, 'users/profile.html')

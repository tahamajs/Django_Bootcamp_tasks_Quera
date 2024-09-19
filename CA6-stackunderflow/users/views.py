from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm
from users.models import User


# Create your views here.

def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Create a new user account
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(request, 'you registered successfully')
            # Log the user in
            login(request, user)


            # Redirect to a success page or user profile
            return redirect('users:home')  # Replace 'profile' with the desired URL name or path
        else:
            messages.warning(request,'register unsuccessfully')

    else:
        form = UserRegisterForm()

    return render(request, 'user/user_register_form.html', {'form': form})


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, 'login successful')
                return redirect('users:home')
            else:
                messages.warning(request,'login unsuccessful')
    else:
        form = UserLoginForm()

    return render(request,'user/user_login_form.html',{'form':form})


def user_logout_view(request):
    logout(request)
    return redirect('users:home')


def user_profile_view(request, uid):
    try:
        user = User.objects.get(id = uid)
    except User.DoesNotExist:
        user = None
    return render(request,'user/user_profile_view.html',{'user':user})

def user_profile_edit_view(request):
    user = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page after a successful update
    else:
        form = UserUpdateForm(instance=user)

    return render(request, 'user/user_edit.html', {'form': form})


def user_home_view(request):
    return render(request, 'home.html')

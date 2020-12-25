from django.shortcuts import render,redirect
from django.contrib.auth.views import *
from courses.views import UserRegisterForm
from django.contrib.messages import *


# didnt created yet
def profile(request):
    return render(request, 'profile/profile.html')




class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    success_url = '/'


def logout_prompt(request):
    return render(request, 'auth/logout_prompt.html')

    
class UserLogoutView(LogoutView):
    template_name = 'auth/logout.html'
    

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            success(request, username)
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form':form})


class UserPasswordChange(PasswordChangeView):
    template_name = 'auth/password_change_form.html'

class UserPasswordChangeDone(PasswordChangeDoneView):
    template_name = 'auth/password_change_done.html'
    
from django.shortcuts import render
from .forms import UserForm, UserInformation

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'Login/index.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_info = UserInformation(data=request.POST)

        #check both forms are valid

        if user_form.is_valid() and user_info.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = user_info.save(commit=False)
            profile.user = user

            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']

            profile.save()
            registered = True

        else:
            print(user_form.errors,user_info.errors)

    else:
        user_form = UserForm()
        user_info = UserInformation()


    return render(request,'Login/registration.html',{'uf':user_form,'ui':user_info,'reg':registered})


def loginviews(request):
    if request.method == "POST":
        username = request.POST.get('name')
        password = request.POST.get('pass')
        #username & password match korabo authenticator use kore
        users = authenticate(username=username,password=password)

        if users:
            if users.is_active:
                login(request,users) #authenticator user object return korse
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active!")

        else:
            print("Failed Login.")
            print("Username: {} and Password: {} ".format(username,password))
            return HttpResponse("Invalid Login")

    else:
        return render(request,'Login/login.html',{})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You're logged in.")





from django.shortcuts import render
from .forms import NewUser

# Create your views here.
def index(request):
    return render(request,'Hello/index.html')


def user(request):
    form = NewUser()

    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error! Invalid form.")  

    return render(request,'Hello/user.html',{'former':form})


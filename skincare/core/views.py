from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login ,logout
from .models import Bestsellers
from .models import Bestsellers_combos
from .models import New_Launches
from .models import Moisturize
from .models import AllProducts
# Create your views here.

def home(request):
    mf = Bestsellers.objects.all()
    bs= Bestsellers_combos.objects.all()
    nl= New_Launches.objects.all()
    mu = Moisturize.objects.all()
    al = AllProducts.objects.all()
    return render(request,'core/home.html',{ 'mf': mf, 'bs':bs, 'nl':nl, 'mu':mu, 'al':al})


def about(request):
    return render(request,'core/about.html')

def contact(request):
    return render(request,'core/contact.html')

def allproducts(request):
    return render(request,'core/allproducts.html')

def sign_up(request):
    if request.method=="POST":
     fm=SignUpForm(request.POST)
     if fm.is_valid():
        fm.save()           
        fm=SignUpForm()

    else:
        fm=SignUpForm()
    return render(request,'core/signup.html',{'form':fm})

#LOGIN

def user_login(request):  
    if request.method=="POST":
        fm=AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
         uname=fm.cleaned_data['username']
         upass=fm.cleaned_data['password']
         user = authenticate(username=uname, password=upass)
         if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/') 
     
    else:
        fm=AuthenticationForm()
    return render(request,'core/login.html',{'form':fm})



#Logout
def user_logout(request):
   logout(request)
   return HttpResponseRedirect('/login/')


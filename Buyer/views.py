
from django.shortcuts import render,redirect
from .import forms 
from django.contrib.auth.forms import AuthenticationForm,User,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from post.models import Post
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from Car.models import CarModel


# Create your views here.

def SignUp(request):
    if request.method=='POST':
        signup_form = forms.SignupForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request,'Account Created Successfuly')
            return redirect("signup")
        
    else:
        signup_form = forms.SignupForm()   
    return render(request,"signup.html",{'form':signup_form,})



class Userlogin(LoginView):
    template_name='login.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request,'Logged in Successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request,'Information Incorret')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context ['type']='Login'
        return context




def profile(request):     
    # data=Post.objects.filter(author = request.user) 
    return render(request,"profile.html",)


def userlogout(request):
    logout(request)
    return redirect('homepage')

def updateprofile(request):
    if request.method=='POST':
            form=forms.UserchangeForm(request.POST,instance= request.user)
            if form.is_valid():
                messages.success(request,'Successfuly Updated')
                form.save()
                
    else:
        form=forms.UserchangeForm(instance= request.user)
    return render(request,"updateprofile.html",{'form':form})



def passchange(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Password Updated Successfully')
                update_session_auth_hash(request,form.user)
                return redirect('profile')
            
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,"password.html",{'form':form})
    else:
        return redirect('Login')
    
    
def buy(request,id):
    data=CarModel.objects.filter(pk=id)
    car=CarModel.objects.get(pk=id)
    car.quantity -=1
    car.save()
    return render(request,"profile.html",{'data':data})
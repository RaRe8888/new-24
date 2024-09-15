from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserRegistrationForm, UserLoginForm, UserUpdateForm
from .models import User
from django.contrib import messages
from random import randint

# Create your views here.
def generate_code():
    return randint(100000,999999)

class UserRegistrationView(View):
    form_class = UserRegistrationForm
    def get(self, request):
        form = self.form_class()
        context = {
            'form':form
        }
        return render(request, 'accounts/signup.html',context)
    
    def post(self,request):
        data = request.POST
        form = self.form_class(data=data)

        if form.is_valid():
            form.save()
            messages.success(request,"Mufvaffaqiyatli")
            return redirect('accounts:login')
        context = {
            'form':form
        }
        messages.error(request,"Xatolik bor")
        return render(request, 'accounts/signup.html',context)
    
class UserLoginView(View):
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form':form
        }
        return render(request, 'accounts/login.html',context)
    
    def post(self,request):
        data = request.POST
        form = self.form_class(data=data)
        context = {
            'form':form
        }
        

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request,username=username,password=password)

            if user is not None:
                messages.success(request,"Siz tizimga kirdingiz")
                login(request,user)
                return redirect('index')
            
            messages.error(request,"Foydalanuvchi topilmadi")
            return render(request, 'accounts/login.html',context)
        
        messages.error(request,"login yoki parol xato kiritildi")
        return render(request, 'accounts/login.html',context)

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("index")
    
class UserUpdateView(View):
    form_class = UserUpdateForm

    def get(self, request):
        form = self.form_class()
        context = {
            'form':form
        }
        return render(request, 'accounts/userupdate.html',context)
    
    def post(self,request):

        user = request.user
        data = request.POST
        files = request.FILES

        form = self.form_class(data=data, files=files, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request,"Mufvaffaqiyatli yangilandi")
            return redirect('index')
        context = {
            'form':form
        }
        messages.error(request,"Xatolik bor")
        return render(request, 'accounts/userupdate.html',context)
    
class PasswordResetView(View):

        def get(self,request):
            # form = self.form_class()
            return render(request, "accounts/passwordreset.html")

        def post(self, request):
            code = str(generate_code())
            print(code,'########################')
            username = request.POST.get('username')
            users = User.objects.filter(username=username)
            if users.exists():
                user = users.first()
                user.set_password(code)
                user.save()


                messages.success(request,"parol o'zgartirildi, yangi parol sizga yuborildi")
                return redirect("accounts:login")
            
            messages.error(request,"username topilmadi")
            return render(request, "accounts/passwordreset.html")
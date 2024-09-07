from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserRegistrationForm
from .models import User
# Create your views here.


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
            return redirect('index')
        context = {
            'form':form
        }
        return render(request, 'accounts/signup.html',context)
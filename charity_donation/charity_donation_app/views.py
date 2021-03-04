from django.shortcuts import render, HttpResponse
from django.views import View


# Create your views here


class LandingPage(View):
    def get(self, request):
        return render(request, 'index.html')


class AddDonation(View):
    def get(self, request):
        return render(request, 'form.html')


class Login(View):
    def get(self, request):
        # return HttpResponse('hello')
        return render(request, 'login.html')


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

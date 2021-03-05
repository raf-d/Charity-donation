from django.shortcuts import render, HttpResponse
from django.views import View
from .models import Category, Donation, Institution


# Create your views here


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all()
        bags = sum([d.quantity for d in donations])
        institutions = len(set([d.institution for d in donations]))
        return render(request, 'index.html', {'bags': bags, 'institutions': institutions})


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

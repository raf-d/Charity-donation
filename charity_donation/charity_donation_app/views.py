from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse, reverse_lazy
from django.views import View

from .mixins import AjaxFormMixin
from .models import Category, Donation, Institution
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


class LandingPage(View):
    def get(self, request):
        donations = Donation.objects.all()
        bags = sum([d.quantity for d in donations])
        institutions = len(set([d.institution for d in donations]))
        foundations = Institution.objects.filter(type='1')
        ngos = Institution.objects.filter(type='2')
        local_collections = Institution.objects.filter(type='3')
        # print(foundations[0].categories.all())

        return render(request, 'index.html', {'bags': bags,
                                              'institutions': institutions,
                                              'foundations': foundations,
                                              'ngos': ngos,
                                              'local_collections': local_collections
                                              })


class AddDonation(LoginRequiredMixin, View):
    def get(self, request):
        # categories = Category.objects.all()
        categories = Category.objects.all()
        # print(categories)
        institutions = set(Institution.objects.filter(categories__in=categories))
        # print('Institutions ->', set(institutions))
        return render(request, 'form.html', {'categories': categories,
                                             'institutions': institutions
                                             })


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = self.authorise(form)
            if user:
                login(request, user)
                return redirect(reverse('home'))
            else:
                return redirect(reverse('register'))
        else:
            return render(request, 'login.html', {'form': form})

    def authorise(self, form):
        username = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        return user


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home'))


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['email'],
                                     email=form.cleaned_data['email'],
                                     password=form.cleaned_data['password'],
                                     first_name=form.cleaned_data['name'],
                                     last_name=form.cleaned_data['surname']
                                     )
            return redirect(reverse('login'))
        else:
            return render(request, 'register.html', {'form': form})


class UserView(View):
    def get(self, request, user_id):
        user = User.objects.get(id=user_id)
        donations = Donation.objects.filter(user=user_id)
        return render(request, 'user.html', {'user': user, 'donations': donations})


# class AddDonation(LoginRequiredMixin, AjaxFormMixin, View):
#     def get(self, request):
#         # categories = Category.objects.all()
#         categories = Category.objects.all()
#         # print(categories)
#         institutions = set(Institution.objects.filter(categories__in=categories))
#         # print('Institutions ->', set(institutions))
#         return render(request, 'form.html', {'categories': categories,
#                                              'institutions': institutions
#                                              })

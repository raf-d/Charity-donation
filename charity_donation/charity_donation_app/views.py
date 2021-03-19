from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse, reverse_lazy
from django.views import View

from .mixins import AjaxFormMixin
from .models import Category, Donation, Institution
from .forms import RegisterForm, LoginForm, DonationForm
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


# class AddDonation(LoginRequiredMixin, View):
#     def get(self, request):
#         # categories = Category.objects.all()
#         categories = Category.objects.all()
#         # print(categories)
#         institutions = Institution.objects.all()
#         # institutions = set(Institution.objects.filter(categories__in=categories))
#         institution = Institution.objects.get(id=1).categories.all()
#         institution_cat = [inst.categories.all() for inst in institutions]
#         print('All Institutions cat->', institution_cat)
#         print('One Institution categories ->', institution)
#         print([inst.id for inst in institution])
#         return render(request, 'form.html', {'categories': categories,
#                                              'institutions': institutions
#                                              })


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


class AddDonation(LoginRequiredMixin, View):
    def get(self, request):
        # form = DonationForm()
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(request, 'form.html', {'categories': categories,
                                             'institutions': institutions
                                             })

    def post(self, request):
        # quantity = request.POST['bags']
        # categories = request.POST['category']
        # institution = request.POST['organisation']
        # address = request.POST['address']
        # phone_number = request.POST['phone']
        # city = request.POST['city']
        # zip_code = request.POST['zipcode']
        # pick_up_date = request.POST['date']
        # pick_up_time = request.POST['time']
        # pick_up_comment = request.POST['more_info']
        # user = request.user
        # donation = Donation.objects.create(
        #     quantity=quantity,
        #     categories=categories,
        #     institution=institution,
        #     address=address,
        #     phone_number=int(phone_number),
        #     city=city,
        #     zip_code=zip_code,
        #     pick_up_date=pick_up_date,
        #     pick_up_time=pick_up_time,
        #     pick_up_comment=pick_up_comment,
        #     user=user,
        # )
        # donation.save()
        return render(request, 'form-confirmation.html')

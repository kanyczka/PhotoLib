from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from photoalbum.models import Photo
from .forms import LoginForm, AddPhotoForm, ShowAllPhotosForm


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "photoalbum/display.html",
                      {"form": form,
                       "button": "Zaloguj się"})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password) # zwraca Nona jeżeli podaliśmy złe dane
            if user is None:
                form.add_error('username',
                               'Login lub hasło jest niepoprawne')
                return render(request, "photoalbum/index.html",
                              {"form": form,
                               "button": "Zaloguj się"})
            login(request, user)
            return redirect(reverse('index'))


class LogoutView(View):
    def get(self, reqest):
        if reqest.user.is_authenticated:
            logout(reqest)
        return redirect(reverse('index'))


class HomeView(View):
    def get(self, request):
        return render(request, "photoalbum/index.html")


# class ShowAllPhotos(ListView):
#     model = Photo
#     # paginate_by = 10
#     template_name = "photoalbum/index_createList.html"

class ShowAllPhotos(View):
    def get(self, request):
        photos = Photo.objects.all().order_by("user")
        return render(request, "photoalbum/index.html", {"photos": photos})

class AddPhoto(View):
    def get(self, request):
        form = AddPhotoForm()
        return render(request, "photoalbum/display.html", {"form": form,
                                                         "button": "Dodaj fotkę"})
    def post(self, request):
        form = AddPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            return render(request, "photoalbum/display.html", {"form": form,
                                                               "button": "Dodaj fotkę"})



    # user = request.user

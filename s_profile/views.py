from django.shortcuts import render


# Create your views here.


def register(request):
    return render(request, 's_profile/register.html')


def profile_view(request):
    return render(request, 's_profile/profile.html')


def login(request):
    return render(request, 's_profile/login.html')


def verif(request):
    return render(request, 's_profile/email_verification.html')

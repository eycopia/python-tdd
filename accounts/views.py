from django.shortcuts import redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Token


def login(request):
    token = request.GET['token']
    # data = Token.objects.find(uuid=token)
    # if data == None:
    return redirect('/');

def send_login_email(request):
    email = request.POST['email']
    send_mail(
        'Your login link for Superlists',
        'Use this link to log in',
        'noreply@superlists',
        [email]
    )
    messages.success(
        request,
        "Check your email, we've sent you a link can use to log in."
    )
    return redirect('/')
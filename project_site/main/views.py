from django.shortcuts import render
from .models import Reviews, Settings
from datetime import datetime, timedelta
from django.http import JsonResponse, HttpResponseNotFound
from django.core.mail import send_mail, EmailMessage


def index(request):
    settings = Settings.objects.all()[0]
    number = settings.number
    address = settings.address
    mail = settings.mail
    if len(address) < 10:
        address = ""
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        if request.POST.get('name') and request.POST.get('number'):
            email = EmailMessage('Новая заявка на сайте "Гермес Консалтинг',f"Имя: {request.POST.get('name')}\nНомер телефона: {request.POST.get('number')}",  "sunclub.stor@gmail.com",
                      ["ilgar.bagishev@gmail.com", mail])
            email.send()
            return JsonResponse({"status": 'success'})
        else:
            return JsonResponse({"status": 'fail'})
    return render(request, "index.html", {"number": number, "address": address, "mail": mail})


def reviews(request):
    settings = Settings.objects.all()[0]
    number = settings.number
    address = settings.address
    mail = settings.mail
    if len(address) < 10:
        address = ""
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        if request.POST.get('name') and request.POST.get('review'):
            if len(request.POST.get('review')) < 10:
                return JsonResponse({"status": 'short'})
            email = EmailMessage('Новый отзыв на сайте "Гермес Консалтинг"',f"Имя: {request.POST.get('name')}\nОтзыв: {request.POST.get('review')}",  "sunclub.stor@gmail.com",
                      ["ilgar.bagishev@gmail.com", mail])
            email.send()
            return JsonResponse({"status": 'success'})
        else:
            return JsonResponse({"status": 'fail'})

    mas = []
    for review in Reviews.objects.all():
        mas.append({'name': review.name, 'review': review.review, 'date': str((review.date + timedelta(hours=3)).strftime("%d.%m.%Y %H:%M"))})
    return render(request, 'reviews.html', {'reviews': mas, "number": number, "address": address, "mail": mail})


def contacts(request):
    settings = Settings.objects.all()[0]
    number = settings.number
    address = settings.address
    mail = settings.mail
    if len(address) < 10:
        address = ""
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        if request.POST.get('name') and request.POST.get('number') and request.POST.get('email') and request.POST.get('message'):
            if request.POST.get('checked') == 'true':
                email = EmailMessage('Новая заявка на сайте "Гермес Консалтинг"',f"Имя: {request.POST.get('name')}\nНомер телефона: {request.POST.get('number')}\nEmail: {request.POST.get('email')}\nСообщение: {request.POST.get('message')}",
                           "sunclub.stor@gmail.com",
                          ["ilgar.bagishev@gmail.com"])
                email.send()
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'not_checked'})
        else:
            return JsonResponse({"status": 'fail'})
    return render(request, 'contacts.html', {"number": number, "address": address, "mail": mail})


def personal_data(request):
    settings = Settings.objects.all()[0]
    number = settings.number
    address = settings.address
    mail = settings.mail
    if len(address) < 10:
        address = ""
    return render(request, 'personal_data.html', {"number": number, "address": address, "mail": mail})

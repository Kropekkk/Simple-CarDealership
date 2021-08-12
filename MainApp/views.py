from django.shortcuts import render

from .models import Offer


def index(request):
    offers = Offer.objects.all()
    return render(request,"MainApp/index.html",
    {
        'offers': offers
    })
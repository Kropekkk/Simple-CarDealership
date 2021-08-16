from django.shortcuts import render

from .models import Offer


def index(request):
    offers = Offer.objects.all()
    return render(request,"MainApp/index.html",{
        'offers': offers
    })

def car(request, offer_id, offer_brand):
    selected = Offer.objects.get(id=offer_id,brand=offer_brand)
    return render(request, "MainApp/car.html",{
        'offer': selected
    })
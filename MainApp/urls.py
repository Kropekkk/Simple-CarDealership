from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("cars/<int:offer_id>/<offer_brand>",views.car, name="car")
]

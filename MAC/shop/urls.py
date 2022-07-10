from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="Shop"),
    path("about/",views.about,name="AboutUs"),
    path("contact/",views.contact,name="ContacUs"),
    path("tracker/", views.tracker, name="TrackeOrder"),
    path("search/", views.search, name="Search"),
    path("productView/<int:myid>", views.pview, name="ProductView"),
    path("checkout/", views.checkout, name="Checkout"),
]
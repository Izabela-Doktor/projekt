from django.contrib import admin
from django.urls import path
from hobby import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("polecane/", views.polecane, name="polecane"),
    path("gatunki/", views.gatunki, name="gatunki"),
    path("kontakt/", views.kontakt, name="kontakt"),
]

from django.urls import path
from . import views


urlpatterns=[
    path("", views.index, name="ana-sayfa"),
    path("markalar",views.balansapp, name="markalar"),
    path("markalar/<slug:slug>", views.balansapp_details, name="markalar-details"),



]

# balansapp/details
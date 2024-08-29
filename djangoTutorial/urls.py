from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("tutorials/", include("tutorial.urls")),
    path("admin/", admin.site.urls)
]
from django.contrib import admin
from django.urls import path
from sun_times.views import get_coordinate

urlpatterns = [
    path("admin/", admin.site.urls),
    path("coordinate/", get_coordinate, name="coordinate"),
]

from django.contrib import admin
from django.urls import path
from hr import views


urlpatterns = [
    # Admin Panel Path
    path("admin/", admin.site.urls),
    # Home Page Path
    path("", views.home, name="home"),
    # Opportunities Path
    path("opportunities/", views.opportunities, name="opportunities"),
]

from django.contrib import admin
from django.urls import path, include
from hr import views


urlpatterns = [
    # Admin Panel Path
    path("admin/", admin.site.urls),
    # ============= FRONTEND SESSION =====================================
    # Home Page Path
    path("", views.home, name="home"),
    # Opportunities Path
    path("opportunities/", views.opportunities, name="opportunities"),
    # Path to Login / Logout
    path("login/", include("django.contrib.auth.urls")),
    # Path to Support
    path("support/", views.support, name="support"),
    # Path to Message
    path("add_message/", views.add_message, name="add_message"),
    # ============= SEND EMAIL =====================================
    # Path to send frontend form
    path("email_frontend/", views.email_frontend, name="email_frontend"),
    # Path to send backend form
    path("email_backend/", views.email_backend, name="email_backend"),
    # Path to send fullstack form
    path("email_fullstack/", views.email_fullstack, name="email_fullstack"),
    # ================= BACKEND SECTION ====================
    path("backend/", views.backend, name="backend"),
]

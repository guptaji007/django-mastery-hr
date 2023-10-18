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
    # Path to FAQ
    path("faq/", views.faq, name="faq"),
    # ============= SEND EMAIL =====================================
    # Path to send frontend form
    path("email_frontend/", views.email_frontend, name="email_frontend"),
    # Path to send backend form
    path("email_backend/", views.email_backend, name="email_backend"),
    # Path to send fullstack form
    path("email_fullstack/", views.email_fullstack, name="email_fullstack"),
    # Path to send intern form
    path("email_intern/", views.email_intern, name="email_intern"),
    # ================= BACKEND SECTION ====================
    # Path to Backend Home Page
    path("backend/", views.backend, name="backend"),
    # Path to Notepad
    path("edit_notepad/", views.edit_notepad, name="edit_notepad"),
]

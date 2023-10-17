from django.shortcuts import render
from django.http import HttpResponseRedirect  # redirect the page after submit
from django.contrib import messages  # send alert message to frontend
from django.core.mail import EmailMultiAlternatives  # required to send mails
from django.template import loader  # render templates on email body
from .models import Registered_email
from django.contrib.auth.decorators import (
    login_required,
)  # Login required to access private pages
from django.views.decorators.cache import (
    cache_control,
)  # Destory the session after the logout


# ================= FRONTEND SECTION ====================
# Home Page View
def home(request):
    return render(request, "home.html")


# Opportunities View
def opportunities(request):
    return render(request, "opportunities.html")


# ================= RESUMES ====================
# Frontend From View
def email_frontend(request):
    if request.method == "POST":
        # Check if email already exist in DB
        email = request.POST["email"]
        if Registered_email.objects.filter(email=email).exists():
            message.error(request, "We already have your resume in our DB.")
            return HttpResponseRedirect("/opportunities")
        else:
            name = request.POST.get("name")
            age = request.POST.get("age")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            address = request.POST.get("address")
            experience = request.POST.get("experience")
            skills = request.POST.get("skills")

            # Register inside DB
            contact = Registered_email()
            contact.email = email
            contact.save()

            template = loader.get_template("resume_form.txt")
            context = {
                "name": name,
                "age": age,
                "email": email,
                "phone": phone,
                "address": address,
                "experience": experience,
                "skills": skills,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                "Frontend - Canidate",
                message,
                "Frontend Opportunity",
                ["demo@gmail.com"],
            )
            email.content_subtype = "html"
            file = request.FILES["file"]
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, "Frontend Resume Sent Successfully !")
            return HttpResponseRedirect("/")


# Backend From View
def email_backend(request):
    if request.method == "POST":
        # Check if email already exist in DB
        email = request.POST["email"]
        if Registered_email.objects.filter(email=email).exists():
            message.error(request, "We already have your resume in our DB.")
            return HttpResponseRedirect("/opportunities")
        else:
            name = request.POST.get("name")
            age = request.POST.get("age")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            address = request.POST.get("address")
            experience = request.POST.get("experience")
            skills = request.POST.get("skills")

            # Register inside DB
            contact = Registered_email()
            contact.email = email
            contact.save()

            template = loader.get_template("resume_form.txt")
            context = {
                "name": name,
                "age": age,
                "email": email,
                "phone": phone,
                "address": address,
                "experience": experience,
                "skills": skills,
            }
            message = template.render(context)
            email = EmailMultiAlternatives(
                "Backend - Canidate", message, "Backend Opportunity", ["demo@gmail.com"]
            )
            email.content_subtype = "html"
            file = request.FILES["file"]
            email.attach(file.name, file.read(), file.content_type)
            email.send()
            messages.success(request, "Backend Resume Sent Successfully !")
            return HttpResponseRedirect("/")


# Fullstack From View
def email_fullstack(request):
    if request.method == "POST":
        # Check if email already exist in DB
        email = request.POST["email"]
        if Registered_email.objects.filter(email=email).exists():
            message.error(request, "We already have your resume in our DB.")
            return HttpResponseRedirect("/opportunities")
    else:
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        experience = request.POST.get("experience")
        skills = request.POST.get("skills")

        # Register inside DB
        contact = Registered_email()
        contact.email = email
        contact.save()

        template = loader.get_template("resume_form.txt")
        context = {
            "name": name,
            "age": age,
            "email": email,
            "phone": phone,
            "address": address,
            "experience": experience,
            "skills": skills,
        }
        message = template.render(context)
        email = EmailMultiAlternatives(
            "Fullstack - Canidate", message, "Fullstack Opportunity", ["demo@gmail.com"]
        )
        email.content_subtype = "html"
        file = request.FILES["file"]
        email.attach(file.name, file.read(), file.content_type)
        email.send()
        messages.success(request, "Fullstack Resume Sent Successfully !")
        return HttpResponseRedirect("/")


# ================= BACKEND SECTION ====================
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    return render(request, "backend.html")

from django.shortcuts import render
from django.http import HttpResponseRedirect  # redirect the page after submit
from django.contrib import messages  # send alert message to frontend
from django.core.mail import EmailMultiAlternatives  # required to send mails
from django.template import loader  # render templates on email body


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
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        experience = request.POST.get("experience")
        skills = request.POST.get("skills")
        file = request.POST.get("file")

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
            "Frontend - Canidate", message, "Frontend Opportunity", ["demo@gmail.com"]
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
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        experience = request.POST.get("experience")
        skills = request.POST.get("skills")
        file = request.POST.get("file")

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
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        experience = request.POST.get("experience")
        skills = request.POST.get("skills")
        file = request.POST.get("file")

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

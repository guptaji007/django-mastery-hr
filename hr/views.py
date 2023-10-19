from django.shortcuts import render
from django.http import HttpResponseRedirect  # redirect the page after submit
from django.contrib import messages  # send alert message to frontend
from django.core.mail import EmailMultiAlternatives  # required to send mails
from django.template import loader  # render templates on email body
from .models import Registered_email, Support, Message, Notepad, Vacancies, Countdown
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
    myJob = Vacancies.objects.all()
    myCountdown = Countdown.objects.all()
    return render(
        request, "opportunities.html", {"vacancies": myJob, "countdowns": myCountdown}
    )


# Support View
def support(request):
    if request.method == "POST":
        # Check if email exists in DB
        email = request.POST["email"]
        if Support.objects.filter(email=email).exists():
            messages.info(
                request, "."
            )  # args of message cannot be empty. We use same msg for many
            return HttpResponseRedirect("/support")
        else:
            support = Support()
            message = request.POST.get("message")
            terms = request.POST.get("terms")
            person = request.POST.get("person")
            option = request.POST.get("option")
            email = request.POST.get("email")

            support.message = message
            support.terms = terms
            support.person = person
            support.option = option
            support.email = email

            support.save()
            messages.success(request, "We will review your request !")
            if not request.user.is_authenticated:
                return HttpResponseRedirect("/")
            else:
                return HttpResponseRedirect("/backend")
    else:
        return render(request, "support.html")


# Message View
def add_message(request):
    if request.method == "POST":
        if request.POST.get("message"):
            message = Message()
            message.text = request.POST.get("message")
            message.save()
            messages.success(request, "Message sent successfully !")
            return HttpResponseRedirect("/")
    else:
        return render(request, "home.html")


# FAQ View
def faq(request):
    return render(request, "faq.html")


# ================= RESUMES ====================
# Frontend From View
def email_frontend(request):
    if request.method == "POST":
        # Check if email already exist in DB
        email = request.POST["email"]
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request, "We already have your resume in our DB.")
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
            messages.error(request, "We already have your resume in our DB.")
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
            messages.error(request, "We already have your resume in our DB.")
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


# Intern From View
def email_intern(request):
    if request.method == "POST":
        # Check if email already exist in DB
        email = request.POST["email"]
        if Registered_email.objects.filter(email=email).exists():
            messages.error(request, "We already have your resume in our DB.")
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
            "Intern - Canidate", message, "Intern Opportunity", ["demo@gmail.com"]
        )
        email.content_subtype = "html"
        file = request.FILES["file"]
        email.attach(file.name, file.read(), file.content_type)
        email.send()
        messages.success(request, "Intern Resume Sent Successfully !")
        return HttpResponseRedirect("/")


# ================= BACKEND SECTION ====================
# Backend Home Page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    total = Registered_email.objects.all().count()
    myNote = Notepad.objects.all()
    myJob = Vacancies.objects.all()
    myCountdown = Countdown.objects.all()
    return render(
        request,
        "backend.html",
        {
            "count": total,
            "notepads": myNote,
            "vacancies": myJob,
            "countdowns": myCountdown,
        },
    )


# Notepad View
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def edit_notepad(request):
    if request.method == "POST":
        notepad = Notepad.objects.get(id=request.POST.get("id"))
        if notepad != None:
            notepad.title = request.POST.get("title")
            notepad.text = request.POST.get("text")
            notepad.save()
            messages.success(request, "Notepad Updated Successfully !")
            return HttpResponseRedirect("/backend")


# Job Vacancies View
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def edit_vacancies(request):
    if request.method == "POST":
        vacancy = Vacancies.objects.get(id=request.POST.get("id"))
        if vacancy != None:
            vacancy.frontend = request.POST.get("frontend")
            vacancy.backend = request.POST.get("backend")
            vacancy.fullstack = request.POST.get("fullstack")
            vacancy.intern = request.POST.get("intern")
            vacancy.save()
            messages.success(request, "Job Vacancies Updated!")
            return HttpResponseRedirect("/backend")


# Countdown View
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def edit_countdown(request):
    if request.method == "POST":
        countdown = Countdown.objects.get(id=request.POST.get("id"))
        if countdown != None:
            countdown.timer = request.POST.get("timer")
            countdown.save()
            messages.success(request, "Countdown Updated Successfully!")
            return HttpResponseRedirect("/backend")

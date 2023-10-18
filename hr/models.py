from django.db import models


# Create your models here.
class Registered_email(models.Model):
    """
    Prevent Duplicate Email
    """

    email = models.CharField(max_length=40)

    def __str__(self):
        return self.email


# Support
class Support(models.Model):
    PERSON = {
        ("Employee", "Employee"),
        ("Candidate", "Candidate"),
    }

    OPTION = {
        ("I lost my account", "I lost my account"),
        ("My password does not world", "My password does not world"),
        ("Update resume", "Update resume"),
        ("Others", "Others"),
    }

    SITUATION = {
        ("Done", "Done"),
        ("Pending", "Pending"),
    }

    terms = models.BooleanField("took responsibility", default=False)
    message = models.TextField()
    person = models.CharField(max_length=50, choices=PERSON)
    option = models.CharField(max_length=50, choices=OPTION)
    email = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(
        max_length=50, null=True, choices=SITUATION, default="Pending"
    )

    def __str__(self):
        return self.person


# Message
class Message(models.Model):
    SITUATION = {
        ("Read", "Read"),
        ("Unread", "Unread"),
    }
    id = models.IntegerField(primary_key=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    situation = models.CharField(
        max_length=50, null=True, choices=SITUATION, default="Unread"
    )

    def __str__(self):
        return self.text


# Notepad
class Notepad(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=60)
    text = models.TextField()

    def __str__(self):
        return self.title


# Job Vacancies
class Vacancies(models.Model):
    id = models.IntegerField(primary_key=True)
    frontend = models.CharField(max_length=100)
    backend = models.CharField(max_length=100)
    fullstack = models.CharField(max_length=100)
    intern = models.CharField(max_length=100)

    def __str__(self):
        return self.frontend

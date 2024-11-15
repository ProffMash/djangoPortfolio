from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def home(request):
    return render(request, 'portfolio/home.html')

def about(request):
    return render(request, 'portfolio/about.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if len(message) < 100:
            messages.error(request, "Message must be at least 100 characters long.")
        else:
            contact = Contact(name=name, email=email, phone=phone, message=message)
            contact.save()
            messages.success(request, "Thank you for contacting us!")
            return redirect('contact')

    return render(request, 'portfolio/contact.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Puppy, CustomerReview, Contact, AdoptionRequest
from .forms import AdoptionForm
from django.core.paginator import Paginator
from random import choice

CONTACT_INFO = {
    'email': 'smallbreedpuppies79@gmail.com',
    'whatsapp': 'https://wa.me/+13862002080'
}

def home(request):
    puppies = Puppy.objects.prefetch_related('images').all()
    random_puppy = choice(puppies) if puppies else None
    reviews = CustomerReview.objects.all()  # Fetch all reviews

    return render(request, 'store/home.html', {
        'puppies': puppies,
        'random_puppy': random_puppy,
        'reviews': reviews,  # Pass reviews to the template
    })

def puppies(request):
    puppies_list = Puppy.objects.all()  # Fetch all puppies
    paginator = Paginator(puppies_list, 6)  # 6 puppies per page
    page_number = request.GET.get('page')
    puppies = paginator.get_page(page_number)
    return render(request, "store/puppies.html", {'puppies': puppies})

def puppy_detail(request, pk):
    puppy = get_object_or_404(Puppy, pk=pk)
    return render(request, 'store/puppy_detail.html', {'puppy': puppy})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Save to the database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        messages.success(request, "Your message has been sent successfully! We'll get back to you soon.")
        return redirect("contact")

    return render(request, "store/contact.html")

from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, get_object_or_404, redirect
from .models import Puppy, AdoptionRequest

def adopt(request, pk):
    puppy = get_object_or_404(Puppy, id=pk)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        # Save the request in the database
        AdoptionRequest.objects.create(
            puppy=puppy,
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        # Email to Admin
        subject_admin = f"New Adoption Request for {puppy.name}"
        body_admin = (
            f"New adoption request submitted:\n\n"
            f"Puppy: {puppy.name}\n"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Message: {message}"
        )

        send_mail(
            subject_admin,
            body_admin,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],  # your admin email
            fail_silently=False,
        )

        # Email to Client
        subject_client = f"Adoption Request Received – {puppy.name}"
        body_client = (
            f"Hi {name},\n\n"
            f"Thank you for your interest in adopting {puppy.name} from Small Size Puppies!\n"
            f"We have received your request and will contact you shortly.\n\n"
            f"Here’s a summary of your submission:\n"
            f"Puppy: {puppy.name}\n"
            f"Breed: {puppy.breed}\n"
            f"Message: {message}\n\n"
            f"Regards,\n"
            f"Small Size Puppies Team"
        )

        send_mail(
            subject_client,
            body_client,
            settings.DEFAULT_FROM_EMAIL,
            [email],  # client's email
            fail_silently=False,
        )

        return render(request, 'store/adopt_success.html', {'puppy': puppy})

    return redirect('puppy_detail', pk=pk)


def thank_you(request):
    return render(request, 'store/thank_you.html', CONTACT_INFO)

def puppy_search(request):
    query = request.GET.get('query', '')
    if query:
        puppies = Puppy.objects.filter(name__icontains=query) | Puppy.objects.filter(breed__icontains=query)
    else:
        puppies = Puppy.objects.all()  # Show all puppies if no query
    return render(request, 'store/puppy_list.html', {'puppies': puppies, 'query': query})

def adoption_agreement(request):
    return render(request, 'store/adoption_agreement.html')

def puppy_list(request):
    puppies = Puppy.objects.all()
    context = {
        'puppies': puppies
    }
    return render(request, 'store/puppy_list.html', context)

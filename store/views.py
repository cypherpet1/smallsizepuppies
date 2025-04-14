from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from .models import Puppy
from .forms import AdoptionForm

CONTACT_INFO = {
    'email': 'your@email.com',
    'whatsapp': 'https://wa.me/237612345678'
}

from .models import Puppy

from random import choice
from .models import Puppy

def home(request):
    puppies = Puppy.objects.prefetch_related('images').all()
    random_puppy = choice(puppies) if puppies else None
    return render(request, 'store/home.html', {
        'puppies': puppies,
        'random_puppy': random_puppy,
    })



from django.core.paginator import Paginator
from django.shortcuts import render

def puppies(request):
    puppies_list = Puppy.objects.all()  # Fetch all puppies
    paginator = Paginator(puppies_list, 6)  # 6 puppies per page
    page_number = request.GET.get('page')
    puppies = paginator.get_page(page_number)
    return render(request, "store/puppies.html", {'puppies': puppies})


def puppy_detail(request, pk):
    puppy = get_object_or_404(Puppy, pk=pk)
    return render(request, 'store/puppy_detail.html', {'puppy': puppy})

from django.contrib import messages



from .models import Contact  # Make sure you've created this model

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



from django.shortcuts import render, get_object_or_404, redirect
from .models import Puppy, AdoptionRequest

def adopt(request, pk):
    puppy = get_object_or_404(Puppy, id=pk)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        AdoptionRequest.objects.create(
            puppy=puppy,
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        return render(request, 'store/adopt_success.html', {'puppy': puppy})
    return redirect('puppy_detail', puppy_id=pk)


def thank_you(request):
    return render(request, 'store/thank_you.html', CONTACT_INFO)

# views.py

from django.shortcuts import render
from .models import Puppy

def puppy_search(request):
    query = request.GET.get('query', '')
    if query:
        puppies = Puppy.objects.filter(name__icontains=query) | Puppy.objects.filter(breed__icontains=query)
    else:
        puppies = Puppy.objects.all()  # Show all puppies if no query
    return render(request, 'store/puppy_list.html', {'puppies': puppies, 'query': query})




def adoption_agreement(request):
    return render(request, 'store/adoption_agreement.html')
from django.shortcuts import render
from .models import Puppy

def puppy_list(request):
    puppies = Puppy.objects.all()
    context = {
        'puppies': puppies
    }
    return render(request, 'store/puppy_list.html', context)

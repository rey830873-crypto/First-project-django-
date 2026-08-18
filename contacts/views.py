from django.shortcuts import render, get_object_or_404
from .models import Contact

def liste_contacts(request):
    contacts = Contact.objects.all().order_by('nom')
    return render(request, 'contacts/liste.html', {'contacts': contacts})

def detail_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'contacts/detail.html', {'contact': contact})
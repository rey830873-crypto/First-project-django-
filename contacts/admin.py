from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'telephone', 'date_ajout')
    search_fields = ('nom', 'prenom', 'email')
    list_filter = ('date_ajout',)
    ordering = ('-date_ajout',)

admin.site.register(Contact, ContactAdmin)
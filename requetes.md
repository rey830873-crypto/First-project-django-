# Requêtes ORM

## Requête 1 : Tous les contacts
Contact.objects.all()
# Résultat : <QuerySet [<Contact: HERVE REGINA EDERE>, <Contact: KETSIA MARIE KOUADIO>, <Contact: CHRIST ALEXINE EDERE>, <Contact: EVRA WILFRIED GUEI>, <Contact: MODESTE JUNIOR BI>, <Contact: AHOU ODILE BOHOUSSOU>]>

## Requête 2 : Filtré par nom
Contact.objects.filter(nom="EDERE")
# Résultat : <QuerySet [<Contact: HERVE REGINA EDERE>, <Contact: CHRIST ALEXINE EDERE>]>

## Requête 3 : Triés par date
Contact.objects.all().order_by('-date_ajout')
# Résultat : <QuerySet [<Contact: AHOU ODILE BOHOUSSOU>, <Contact: MODESTE JUNIOR BI>, <Contact: EVRA WILFRIED GUEI>, <Contact: CHRIST ALEXINE EDERE>, <Contact: KETSIA MARIE KOUADIO>, <Contact: HERVE REGINA EDERE>]>
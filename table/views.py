from django.shortcuts import render
from django.http import HttpResponse

def accueil(request):
    return HttpResponse("L'URL est incomplète...")

def table_view(request, col1, col2, col3, col4, col5, col6):
    # Séparer les valeurs de col4 et col5 en listes
    etage_1_values = col4.split(";")
    etage_2_values = col5.split(";")
    etage_3_values = col6.split(";")

    # Vérifier que chaque colonne contient bien 5 éléments (optionnel)
    if len(etage_1_values) != 5 or len(etage_2_values) != 5:
        return HttpResponse("Erreur : les colonnes 'Etage 1' et 'Etage 2' doivent contenir 5 valeurs séparées par ';'.")

    # Contexte pour le template
    context = {
        'col1': col1,
        'col2': col2,
        'col3': col3,
        'etage_1_values': etage_1_values,
        'etage_2_values': etage_2_values,
        'etage_3_values': etage_3_values,
    }
    
    return render(request, 'table.html', context)




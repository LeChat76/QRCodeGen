from django.shortcuts import render
from django.http import HttpResponse

def accueil(request):
    return HttpResponse("L'url est incomplet....")

def table_view(request, col1, col2, col3, col4, col5):
    context = {
        'col1': col1,
        'col2': col2,
        'col3': col3,
        'col4': col4,
        'col5': col5,
    }
    return render(request, 'table/table.html', context)



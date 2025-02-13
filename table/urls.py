from django.urls import path
from .views import table_view, accueil

urlpatterns = [
    path('', accueil, name='accueil'),
    path('table/<str:col1>/<str:col2>/<str:col3>/<str:col4>/<str:col5>/<str:col6>/', table_view, name='table_view'),
]


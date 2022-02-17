from django.urls import path
from aperitivos.views import videos, indice

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', videos, name='video'),
    path('', indice, name='indice'),
]

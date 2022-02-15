from django.urls import path
from aperitivos.views import videos

app_name = 'aperitivos'
urlpatterns = [
    path('<slug:slug>', videos, name='video'),
]

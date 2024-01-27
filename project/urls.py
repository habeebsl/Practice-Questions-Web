from django.urls import path
from .views import questionView

urlpatterns = [
    path('', questionView, name='question'),
]
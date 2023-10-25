
from django.urls import path
from .views import createAuthor, createBooks, getBooknamesFromAuthor

urlpatterns = [
    path('createAuthor',createAuthor),
    path('createBooks',createBooks),
    path('getBooknamesFromAuthor',getBooknamesFromAuthor)
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('games', views.games, name='games'),
    path('test', views.test, name='test'),
    path('contact', views.contact, name="contact"),
    path('error', views.error, name='error'),
    path('about', views.about, name='about'),
    path('nobuy', views.nobuy, name='nobuy'),
    path('search', views.search, name="search")
]

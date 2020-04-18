from django.urls import path

from .views import *


urlpatterns = [
   path('', index, name='index'),
   path('empresas', company, name='company_home'),
   path('candidato', candidate, name='candidate_home'),
]

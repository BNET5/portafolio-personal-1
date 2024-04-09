from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class index(TemplateView):
    template_name = 'index.html' #especifica la ubicacion de tu plantilla


    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #context['nombre'] = 'Victor Hugo Cruz Amaru'
        #return context

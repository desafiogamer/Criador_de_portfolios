from django.shortcuts import render
from django.urls import reverse_lazy
from. forms import UsuarioForms
from django.views.generic.edit import CreateView

# Create your views here.

class UsuarioCreate(CreateView):
    template_name = 'formregistrar.html'
    form_class = UsuarioForms
    success_url = reverse_lazy('index')
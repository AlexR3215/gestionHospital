from django.shortcuts import render
from django.views.generic.base import TemplateView
from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Hospital, Medico, Paciente
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.

class InicioView(TemplateView): 
    template_name = "core/portada.html"


class listadoHospitales(ListView):
    template_name = "core/listadoHospitales_list.html"
    model = Hospital


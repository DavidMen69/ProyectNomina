from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from .models import Departamento
# Create your views here.
def BASE(request):
    return render(request, 'base.html')

# Lista de departamentos
class DepartamentoListView(ListView):
    model = Departamento
    template_name = 'departamento_list.html'
    context_object_name = 'departamentos'

# Crear un departamento
class DepartamentoCreateView(CreateView):
    model = Departamento
    template_name = 'departamento_create.html'
    fields = ['nom_departamento', 'estado']
    success_url = '/departamentos/'  # Redirigir a la lista de departamentos después de crear uno

# Actualizar un departamento

class DepartamentoUpdateView(UpdateView):
    model = Departamento
    template_name = 'departamento_update.html'
    fields = ['nom_departamento', 'estado']
    success_url = '/departamentos/'  # Redirigir a la lista de departamentos después de crear uno

# Eliminar un departamento

class DepartamentoDeleteView(DeleteView):
    model = Departamento
    template_name = 'departamento_delete.html'
    success_url = '/departamentos/'  # Redirigir a la lista de departamentos después de eliminar uno
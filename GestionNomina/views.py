from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Departamento, Cargo, Empleado

# Define una vista llamada BASE que renderiza la plantilla 'base.html'.
def BASE(request):
    return render(request, 'base.html')

# Define una vista de lista para los departamentos.
class DepartamentoListView(ListView):
    # Establece el modelo que se utilizará para esta vista.
    model = Departamento
    # Establece la plantilla que se utilizará para renderizar la lista de departamentos.
    template_name = 'departamento_list.html'
    # Establece el nombre de contexto que se utilizará en la plantilla para referirse a la lista de departamentos.
    context_object_name = 'departamentos'

# Define una vista para crear un nuevo departamento.
class DepartamentoCreateView(CreateView):
    # Establece el modelo que se utilizará para crear el departamento.
    model = Departamento
    # Establece la plantilla que se utilizará para el formulario de creación de departamento.
    template_name = 'departamento_create.html'
    # Especifica los campos del modelo que se mostrarán en el formulario.
    fields = ['nom_departamento', 'estado']
    # Establece la URL a la que se redirigirá después de crear exitosamente un departamento.
    success_url = '/departamentos/'

# Define una vista para actualizar un departamento existente.
class DepartamentoUpdateView(UpdateView):
    # Establece el modelo que se utilizará para actualizar el departamento.
    model = Departamento
    # Establece la plantilla que se utilizará para el formulario de actualización de departamento.
    template_name = 'departamento_update.html'
    # Especifica los campos del modelo que se mostrarán en el formulario de actualización.
    fields = ['nom_departamento', 'estado']
    # Establece la URL a la que se redirigirá después de actualizar exitosamente un departamento.
    success_url = '/departamentos/'

# Define una vista para eliminar un departamento existente.
class DepartamentoDeleteView(DeleteView):
    # Establece el modelo que se utilizará para eliminar el departamento.
    model = Departamento
    # Establece la plantilla que se utilizará para la confirmación de eliminación de departamento.
    template_name = 'departamento_delete.html'
    # Establece la URL a la que se redirigirá después de eliminar exitosamente un departamento.
    success_url = '/departamentos/'

# ------------------Inicio Del Model Cargo--------------------------------

# Lista de Cargo
def listar_cargos(request):
    cargos = Cargo.objects.all()  # Obtener todos los objetos Cargo de la base de datos
    return render(request, 'cargo_list.html', {'cargos': cargos})


# Crear un Cargo
class CargoCreateView(CreateView):
    model = Cargo
    template_name = 'cargo_create.html'
    fields = ['nombre_cargo', 'estado']
    success_url = '/cargos/'  # Redirigir a la lista de cargo después de crear uno

# Actualizar un Cargo

class CargoUpdateView(UpdateView):
    model = Cargo
    template_name = 'cargo_update.html'
    fields = ['nombre_cargo', 'estado']
    success_url = '/cargos/'  # Redirigir a la lista de departamentos después de crear uno

# Eliminar un Cargo

class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = 'cargo_delete.html'
    success_url = '/cargos/'  # Redirigir a la lista de departamentos después de eliminar uno


# ------------------Inicio Del Model Empleado--------------------------------

# Lista de Empleados

def listar_empleados(request):
    empleados = Empleado.objects.all()  # Obtener todos los objetos Empleados de la base de datos
    return render(request, 'empleado_list.html', {'empleados': empleados})

# Crear un Empleados
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleado_create.html'
    fields = ['num_documento', 'nombres','apellido1', 'apellido2','telefono', 'correo','estado']
    success_url = '/empleados/'  # Redirigir a la lista de cargo después de crear uno

#Actualizar Empleados
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'empleado_update.html'
    fields = ['num_documento', 'nombres','apellido1', 'apellido2','telefono', 'correo','estado']
    success_url = '/empleados/'  # Redirigir a la lista de departamentos después de crear uno

# Eliminar un Empleados

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado_delete.html'
    success_url = '/Empleados/'  # Redirigir a la lista de departamentos después de eliminar uno
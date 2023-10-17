from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import Departamento, Cargo, Empleado



# Define una vista llamada BASE que renderiza la plantilla 'base.html'.
def BASE(request):
    return render(request, 'base.html')

# Define una vista de lista para los departamentos.
class DepartamentoListView(ListView):
    # Establece el modelo que se utilizará para esta vista.
    model = Departamento
    # Establece la plantilla que se utilizará para renderizar la lista de departamentos.
    template_name = 'departamento/departamento_list.html'
    # Establece el nombre de contexto que se utilizará en la plantilla para referirse a la lista de departamentos.
    context_object_name = 'departamentos'


# Define una vista para crear un nuevo departamento.
def crearDepartamento(request):
    nom_departamento = request.POST['txtNombre']
    estado = request.POST['txtEstado'] == "True"
    departamento = Departamento.objects.create(nom_departamento=nom_departamento,estado=estado)
    return redirect('/departamentos/')

# define el detalle del departamento

def detalleDepartamento(request,pk):
    departamento = Departamento.objects.get(id=pk)
    return render(request, 'departamento/detalleDepartamento.html ',{'departamento': departamento})


# Define una vista para actualizar un departamento existente.
def edicionDepartamento(request,pk):
    departamento = Departamento.objects.get(id=pk)
    return render(request, 'departamento/edicionDepartamento.html ',{'departamento': departamento})

def editarDepartamento(request,pk):
    departamento = Departamento.objects.get(id=pk)
    if request.method == 'POST':
        nom_departamento = request.POST['txtNombre']
        estado = request.POST['txtEstado'] == "True"
        departamento.nom_departamento = nom_departamento
        departamento.estado = estado
        departamento.save()
        return redirect('/departamentos/')


# Define una vista para eliminar un departamento existente.
def eliminarDepartamento(request,pk):
    departamento = Departamento.objects.get(id=pk)
    departamento.delete()
    return redirect('/departamentos/')

# ------------------Inicio Del Model Cargo--------------------------------

# Lista de Cargo
def listar_cargos(request):
    cargos = Cargo.objects.all()  # Obtener todos los objetos Cargo de la base de datos
    return render(request, 'cargo/cargo_list.html', {'cargos': cargos})


# Crear un Cargo
def get_departamento(request):
    departamentos = list(Departamento.objects.values())

    if (len(departamentos)>0):
        data = {'message':"success", 'departamentos':departamentos}
    else:
        data = {'message':"Not Found"}

    return JsonResponse(data)

def crearCargo(request):
    nom_departamento = request.POST['txtNombre']
    estado = request.POST['txtEstado'] == "True"
    departamento = Departamento.objects.create(nom_departamento=nom_departamento,estado=estado)
    return redirect('/cargos/')


# Actualizar un Cargo

class CargoUpdateView(UpdateView):
    model = Cargo
    template_name = 'cargo_update.html'
    fields = ['nombre_cargo', 'estado']
    success_url = '/cargos/'  # Redirigir a la lista de cargo después de crear uno

# Eliminar un Cargo

class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = 'cargo_delete.html'
    success_url = '/cargos/'  # Redirigir a la lista de cargo después de eliminar uno


# ------------------Inicio Del Model Empleado--------------------------------

# Lista de Empleados

def listar_empleados(request):
    empleados = Empleado.objects.all()  # Obtener todos los objetos Empleados de la base de datos
    return render(request, 'empleado/empleado_list.html', {'empleados': empleados})

# Crear un Empleados
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'empleado_create.html'
    fields = ['num_documento', 'nombres','apellido1', 'apellido2','telefono', 'correo','estado']
    success_url = '/empleados/'  # Redirigir a la lista de empleado después de crear uno

#Actualizar Empleados
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = 'empleado_update.html'
    fields = ['num_documento', 'nombres','apellido1', 'apellido2','telefono', 'correo','estado']
    success_url = '/empleados/'  # Redirigir a la lista de empleado después de crear uno

# Eliminar un Empleados

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'empleado_delete.html'
    success_url = '/Empleados/'  # Redirigir a la lista de empleado después de eliminar uno
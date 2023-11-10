from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.views.generic import ListView
from .models import Departamento, Cargo, Empleado
from django.shortcuts import render, get_object_or_404

def CONTACTO(request):
    return render(request, 'contacto.html')
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
    if request.method == 'POST':
        departamento_id = request.POST.get('departamento')  # Obtener el ID del departamento seleccionado
        nombre_cargo = request.POST.get('txtNombre')
        estado = request.POST.get('txtEstado') == "True"

        # Verificar si el departamento seleccionado existe
        try:
            departamento = Departamento.objects.get(id=departamento_id)
        except Departamento.DoesNotExist:
            # Manejar el caso en el que el departamento no existe
            return HttpResponse("Departamento no encontrado")

        # Crear el cargo y asignarlo al departamento
        cargo = Cargo.objects.create(nombre_cargo=nombre_cargo, estado=estado, departamento=departamento)
        return redirect('/cargo')
    else:
        # Lógica para manejar el método GET, si es necesario
        return HttpResponse("Acceso no válido")



def edicionCargo(request, cargo_id):
    try:
        cargo = get_object_or_404(Cargo, pk=cargo_id)
        departamentos = Departamento.objects.all()  # Obtén todos los departamentos

        return render(request, 'cargo/edicionCargo.html', {'cargo': cargo, 'departamentos': departamentos})
    except Cargo.DoesNotExist:
        return JsonResponse({'message': 'error', 'error': 'Cargo no encontrado'}, status=404)

def editarCargo(request, cargo_id):
    cargo = get_object_or_404(Cargo, pk=cargo_id)

    if request.method == 'POST':
        departamento_id = request.POST.get('departamento')
        nombre_cargo = request.POST.get('txtNombre')
        estado = request.POST.get('txtEstado') == "True"

        try:
            departamento = Departamento.objects.get(id=departamento_id)
        except Departamento.DoesNotExist:
            return HttpResponse("Departamento no encontrado")

        cargo.nombre_cargo = nombre_cargo
        cargo.estado = estado
        cargo.departamento = departamento
        cargo.save()

        return HttpResponseRedirect('/cargo')  # Redirigir a la lista de cargos

    return render(request, 'cargo/edicionCargo.html', {'cargo': cargo})
# Eliminar un Cargo

def detalleCargo(request,cargo_id):
    try:
        cargo = Cargo.objects.get(pk=cargo_id)
        return render(request, 'cargo/detalleCargo.html',{'cargo': cargo})
    except Cargo.DoesNotExist:
        return JsonResponse({'message': 'error', 'error': 'Cargo no encontrado'}, status=404)


# ------------------Inicio Del Model Empleado--------------------------------

# Lista de Empleados

def listar_empleados(request):
    empleados = Empleado.objects.all()  # Obtener todos los objetos Empleados de la base de datos
    return render(request, 'empleado/empleado_list.html', {'empleados': empleados})



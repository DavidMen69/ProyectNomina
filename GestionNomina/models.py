from django.db import models

# Create your models here.
# Definir el modelo 'Departamento'.


class Departamento(models.Model):
    # Campo para almacenar el nombre del departamento.
    nom_departamento = models.CharField(max_length=50, verbose_name='Nombre Del Departamento')
    
    # Campo para almacenar el estado del departamento (activo/inactivo).
    estado = models.BooleanField(default=False)
    
    # Campo para almacenar la fecha de registro, que se establecerá automáticamente en la creación.
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    # Método para proporcionar una representación legible por humanos de una instancia del modelo.
    def __str__(self):
        return self.nom_departamento

class Cargo(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    nombre_cargo = models.CharField(max_length=50, verbose_name='Nombre Del Cargo')

    estado = models.BooleanField(default=False)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_cargo


# Definir el modelo 'Empleado'.
class Empleado(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.CASCADE,
        default=1,
        limit_choices_to={'departamento': models.F('departamento')}
    )

    # Campo para almacenar el número de documento del empleado.
    num_documento = models.CharField(max_length=30, verbose_name='Numero De Documento')
    
    # Campo para almacenar los nombres del empleado.
    nombres = models.CharField(max_length=60)
    
    # Campo para almacenar el primer apellido del empleado.
    apellido1 = models.CharField(max_length=30, verbose_name='Apellido Paterno')
    
    # Campo para almacenar el segundo apellido del empleado.
    apellido2 = models.CharField(max_length=30, verbose_name='Apellido Materno')
    
    # Campo para almacenar el número de teléfono del empleado.
    telefono = models.CharField(max_length=20)
    
    # Campo para almacenar la dirección de correo electrónico del empleado.
    correo = models.CharField(max_length=50)
    
    # Campo para almacenar el estado del empleado (activo/inactivo).
    estado = models.BooleanField(default=False)
    
    # Campo para almacenar la fecha de registro, que se establecerá automáticamente en la creación.
    fecha_Registro = models.DateTimeField(auto_now_add=True)
    
    # Método para proporcionar una representación legible por humanos de una instancia del modelo.
    def __str__(self):
        return f'{self.nombres} {self.apellido1} {self.apellido2}'


class Nomina(models.Model):
    # Clave primaria autogenerada

    # Pueades agregr otros campos relacionados a la nómina aquí

    # Clave foránea para relacionar la nómina con un empleado

    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    sal_base = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    sal_final = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    transporte = models.CharField(max_length=10)

    hora_extra = models.IntegerField()

    dominicales = models.IntegerField()

    diurna = models.IntegerField()

    nocturnas = models.IntegerField()

    recargo_nocturno = models.IntegerField()

    festivos = models.IntegerField()

    devengado = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    estado = models.BooleanField(default=False)

    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Nómina de {self.empleado.nombres} {self.empleado.apellido1} {self.empleado.apellido2}'

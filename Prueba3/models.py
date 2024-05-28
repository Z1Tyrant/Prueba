from django.db import models

# Create your models here.

class Memorial(models.Model):
    id_memorial = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12)
    dv = models.CharField(max_length=1)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    fecha_fallecimiento = models.DateField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.id_memorial})"
    
    
class UsuarioMemorial(models.Model):
    id_memorial_usuario = models.AutoField(primary_key=True)
    memorial = models.ForeignKey(Memorial, on_delete=models.CASCADE, related_name='usuarios_memorial')

    def __str__(self):
        return f"UsuarioMemorial {self.id_memorial_usuario} para Memorial {self.memorial.id_memorial}"


class Recuerdos(models.Model):
    id_recuerdos = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    introduccion = models.TextField()
    recuerdo = models.TextField()
    foto = models.ImageField(upload_to='fotos_recuerdos/', blank=True, null=True)
    usuario_memorial = models.ForeignKey(UsuarioMemorial, on_delete=models.CASCADE, related_name='recuerdos')

    def __str__(self):
        return f"Recuerdo {self.nombre} para UsuarioMemorial {self.usuario_memorial.id_memorial_usuario}" 
    
    
class Parentescos(models.Model):
    id_parentesco = models.AutoField(primary_key=True)
    parentesco = models.CharField(max_length=100)
    descrpcion = models.CharField(max_length=255)
    usuario_memorial = models.ForeignKey(UsuarioMemorial, on_delete=models.CASCADE, related_name='parentescos')

    def __str__(self):
        return f"Parentesco {self.parentesco} para UsuarioMemorial {self.usuario_memorial.id_memorial_usuario}" 
    

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='ciudades')

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    comuna = models.CharField(max_length=100)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, related_name='comunas')

    def __str__(self):
        return self.comuna
    
    

    



    
    
    
class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    fecha_pago = models.DateField()

    def __str__(self):
        return f"Pago {self.id_pago}"
    
class Suscripciones(models.Model):
    id_suscripcion = models.AutoField(primary_key=True)
    fecha_suscripcion = models.DateField()
    estado = models.BooleanField(default=True)

 
    pagos = models.OneToManyField(Pago, on_delete=models.CASCADE, related_name='suscripcion')

    def __str__(self):
        return f"Suscripción {self.id_suscripcion}"
    
    
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    correo = models.EmailField(unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)
    dv = models.CharField(max_length=1)
    direccion = models.CharField(max_length=255)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, related_name='usuarios')

    usuario_memoriales = models.OneToManyField(UsuarioMemorial, on_delete=models.CASCADE, related_name='usuario')
    suscripciones = models.OneToManyField(Suscripciones, on_delete=models.CASCADE, related_name='usuario')

    def __str__(self):
        return f"{self.nombres} {self.apellidos}" 
    
    
class Plan(models.Model):
    id_plan = models.AutoField(primary_key=True)
    nombre_plan = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad_memoriales = models.IntegerField()

    suscripciones = models.OneToManyField(Suscripciones, on_delete=models.CASCADE, related_name='plan')
    memoriales = models.OneToManyField(Memorial, on_delete=models.CASCADE, related_name='plan')

    def __str__(self):
        return self.nombre_plan
       
    
    



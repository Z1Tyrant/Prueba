from django.contrib import admin
from .models import Memorial, UsuarioMemorial, Recuerdos, Parentescos, Region, Ciudad, Comuna, Pago, Suscripciones, Usuario, Plan

# Register your models here.

admin.site.register(Memorial)
admin.site.register(UsuarioMemorial)
admin.site.register(Recuerdos)
admin.site.register(Parentescos)
admin.site.register(Region)
admin.site.register(Ciudad)
admin.site.register(Comuna)
admin.site.register(Pago)
admin.site.register(Suscripciones)
admin.site.register(Usuario)
admin.site.register(Plan)
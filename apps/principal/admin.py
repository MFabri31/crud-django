from django.contrib import admin

# Register your models here.
from .models import Person

# Registra el modelo Person en el panel de admin.
admin.site.register(Person)

from django.db import models

# Create your models here.


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    lastName = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)

    def __str__(self):
        """Muestra el nombre de cada instancia del modelo en el panel de admin."""
        return self.name



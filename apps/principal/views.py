from django.shortcuts import render, redirect

# Create your views here.
from .models import Person
from .forms import PersonForm


def home(request):
    # Se hace uso del orm. select *  from Person
    persons = Person.objects.all()
    # print(persons)
    context = {
        'persons': persons
    }
    return render(request, 'index.html', context)


def createPerson(request):
    if request.method == 'GET':
        form = PersonForm()
        context = {
            'form': form
        }
    else:
        form = PersonForm(request.POST)
        context = {
            'form': form
        }

        if form.is_valid():
            form.save()                 # Registra los datos en la bd
            return redirect('index')    # Redirecciona a la ruta index

    return render(request, 'register.html', context)


def editPerson(request, id):            # id representa la pk de cada usuario
    person = Person.objects.get(id=id)

    if request.method == 'GET':
        form = PersonForm(instance=person)

        context = {
            'form': form
        }
    else:
        # instance = person - no lo toma como un nuevo contacto, sino como uno existente para modificar.
        form = PersonForm(request.POST, instance=person)
        context = {
            'form': form
        }
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'register.html', context)


def deletePerson(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect('index')


"""


get() -  obtiene un valor de la bd a través del 2do parámetro id. Solo retorna un valor.

"""

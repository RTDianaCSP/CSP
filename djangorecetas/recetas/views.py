from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Ingrediente
from .forms import IngredienteForm

from .models import Plato
from .forms import PlatoForm

from .models import MenuSemanal
from .forms import MenuSemanalForm

def inicio(request):
     return render(request, 'base.html')


# INGREDIENTE

def lista_ingredientes(request):
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingredientes/lista.html', {'ingredientes': ingredientes})


def crear_ingrediente(request):
    form = IngredienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_ingredientes')
    return render(request, 'ingredientes/form.html', {'form': form})


def editar_ingrediente(request, id):
    ingrediente = get_object_or_404(Ingrediente, id=id)
    form = IngredienteForm(request.POST or None, instance=ingrediente)
    if form.is_valid():
        form.save()
        return redirect('lista_ingredientes')
    return render(request, 'ingredientes/form.html', {'form': form})


def eliminar_ingrediente(request, id):
    ingrediente = get_object_or_404(Ingrediente, id=id)
    ingrediente.delete()
    return redirect('lista_ingredientes')

# PLATO

def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, 'platos/lista.html', {'platos': platos})


def crear_plato(request):
    form = PlatoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_platos')
    return render(request, 'platos/form.html', {'form': form})


def editar_plato(request, id):
    plato = get_object_or_404(Plato, id=id)
    form = PlatoForm(request.POST or None, request.FILES or None, instance=plato)
    if form.is_valid():
        form.save()
        return redirect('lista_platos')
    return render(request, 'platos/form.html', {'form': form})

def eliminar_plato(request, id):
    plato = get_object_or_404(Plato, id=id)
    plato.delete()
    return redirect('lista_platos')

# MENU SEMANAL


def lista_menus(request):
    menus = MenuSemanal.objects.all()
    return render(request, 'menus/lista.html', {'menus': menus})


def crear_menu(request):
    form = MenuSemanalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_menus')
    return render(request, 'menus/form.html', {'form': form})

def editar_menu(request, id):
    menu = get_object_or_404(MenuSemanal, id=id)
    form = MenuSemanalForm(request.POST or None, instance=menu)
    if form.is_valid():
        form.save()
        return redirect('lista_menus')
    return render(request, 'menus/form.html', {'form': form})

def eliminar_menu(request, id):
    menu = get_object_or_404(MenuSemanal, id=id)
    menu.delete()
    return redirect('lista_menus')
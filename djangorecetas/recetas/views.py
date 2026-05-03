from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Ingrediente, Plato, MenuSemanal
from .forms import IngredienteForm, PlatoForm, MenuSemanalForm


def inicio(request):
    """
    Vista principal de la aplicación.

    :param request: Solicitud HTTP del usuario.
    :type request: HttpRequest

    :returns: Página principal de la aplicación.
    :rtype: HttpResponse
    """
    return render(request, 'base.html')


# INGREDIENTE

def lista_ingredientes(request):
    """
    Muestra la lista de ingredientes.

    :param request: Solicitud HTTP.
    :type request: HttpRequest

    :returns: Página con la lista de ingredientes.
    :rtype: HttpResponse
    """
    ingredientes = Ingrediente.objects.all()
    return render(request, 'ingredientes/lista.html', {'ingredientes': ingredientes})


def crear_ingrediente(request):
    """
    Crea un nuevo ingrediente.

    :param request: Solicitud HTTP con datos del formulario.
    :type request: HttpRequest

    :returns: Redirección a la lista o formulario con errores.
    :rtype: HttpResponse
    """
    form = IngredienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_ingredientes')
    return render(request, 'ingredientes/form.html', {'form': form})


def editar_ingrediente(request, id):
    """
    Edita un ingrediente existente.

    :param request: Solicitud HTTP.
    :type request: HttpRequest
    :param id: Identificador del ingrediente.
    :type id: int

    :returns: Redirección o formulario de edición.
    :rtype: HttpResponse
    """
    ingrediente = get_object_or_404(Ingrediente, id=id)
    form = IngredienteForm(request.POST or None, instance=ingrediente)
    if form.is_valid():
        form.save()
        return redirect('lista_ingredientes')
    return render(request, 'ingredientes/form.html', {'form': form})


def eliminar_ingrediente(request, id):
    """
    Elimina un ingrediente.

    :param request: Solicitud HTTP.
    :type request: HttpRequest
    :param id: Identificador del ingrediente.
    :type id: int

    :returns: Redirección a la lista de ingredientes.
    :rtype: HttpResponse
    """
    ingrediente = get_object_or_404(Ingrediente, id=id)
    ingrediente.delete()
    return redirect('lista_ingredientes')


# PLATO

def lista_platos(request):
    """
    Muestra la lista de platos.

    :param request: Solicitud HTTP.
    :type request: HttpRequest

    :returns: Página con la lista de platos.
    :rtype: HttpResponse
    """
    platos = Plato.objects.all()
    return render(request, 'platos/lista.html', {'platos': platos})


def crear_plato(request):
    """
    Crea un nuevo plato.

    :param request: Solicitud HTTP con datos y archivos.
    :type request: HttpRequest

    :returns: Redirección o formulario.
    :rtype: HttpResponse
    """
    form = PlatoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lista_platos')
    return render(request, 'platos/form.html', {'form': form})


def editar_plato(request, id):
    """
    Edita un plato existente.

    :param request: Solicitud HTTP.
    :type request: HttpRequest
    :param id: Identificador del plato.
    :type id: int

    :returns: Redirección o formulario de edición.
    :rtype: HttpResponse
    """
    plato = get_object_or_404(Plato, id=id)
    form = PlatoForm(request.POST or None, request.FILES or None, instance=plato)
    if form.is_valid():
        form.save()
        return redirect('lista_platos')
    return render(request, 'platos/form.html', {'form': form})


def eliminar_plato(request, id):
    """
    Elimina un plato.

    :param request: Solicitud HTTP.
    :type request: HttpRequest
    :param id: Identificador del plato.
    :type id: int

    :returns: Redirección a la lista de platos.
    :rtype: HttpResponse
    """
    plato = get_object_or_404(Plato, id=id)
    plato.delete()
    return redirect('lista_platos')


# MENU SEMANAL
def lista_menus(request):
    """
    Muestra los menús semanales.

    :param request: Solicitud HTTP.
    :type request: HttpRequest

    :returns: Página con los menús semanales.
    :rtype: HttpResponse
    """
    menus = MenuSemanal.objects.all()
    return render(request, 'menus/lista.html', {'menus': menus})


def crear_menu(request):
    """
    Crea un nuevo menú semanal.

    :param request: Solicitud HTTP.
    :type request: HttpRequest

    :returns: Redirección o formulario.
    :rtype: HttpResponse
    """
    form = MenuSemanalForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_menus')
    return render(request, 'menus/form.html', {'form': form})


def editar_menu(request, id):
    """
    Edita un menú semanal.

    :param request: Solicitud HTTP.
    :type request: HttpRequest
    :param id: Identificador del menú.
    :type id: int

    :returns: Redirección o formulario de edición.
    :rtype: HttpResponse
    """
    menu = get_object_or_404(MenuSemanal, id=id)
    form = MenuSemanalForm(request.POST or None, instance=menu)
    if form.is_valid():
        form.save()
        return redirect('lista_menus')
    return render(request, 'menus/form.html', {'form': form})


def eliminar_menu(request, id):
    """
    Elimina un menú semanal.

    :param request: Solicitud HTTP.
    :type request: HttpRequest
    :param id: Identificador del menú.
    :type id: int

    :returns: Redirección a la lista de menús.
    :rtype: HttpResponse
    """
    menu = get_object_or_404(MenuSemanal, id=id)
    menu.delete()
    return redirect('lista_menus')
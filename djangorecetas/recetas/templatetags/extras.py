from django import template

register = template.Library()

@register.filter
def mayusculas(value):
    return value.upper()

@register.filter
def contar_ingredientes(plato):
    return plato.ingredientes.count()

@register.filter
def formato_menu(menu):
    return f"Semana {menu.semana} - {menu.ano}"

@register.simple_tag
def total_platos(menu):
    return menu.platos.count()
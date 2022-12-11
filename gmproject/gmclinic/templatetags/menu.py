from atexit import register
from django import template
from gmclinic.models import Directions

register = template.Library()


@register.inclusion_tag('gm/menu_tpl.html')
def show_menu(menu_class='menu'):
    directions = Directions.objects.all()
    return {"directions": directions, "menu_class": menu_class}

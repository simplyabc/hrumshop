from django import template
from hrumshop.models import *

register = template.Library()

toolbar = [
    {'title': 'Главная страница', 'url_name': 'main'},
    {'title': 'Доставка', 'url_name': 'transport'},
    {'title': 'Контакты', 'url_name': 'contact'},
]


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_toolbar():
    return toolbar

# myapp/templatetags/mycomponents.py

from django_component import Library, Component

register = Library()

@register.component
class Header(Component):
    template = "header.html"

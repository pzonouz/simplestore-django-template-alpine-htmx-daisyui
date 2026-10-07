from django import template

register = template.Library()


@register.filter
def get_attr(obj, attr_name):
    if isinstance(obj, dict):
        return obj.get(attr_name, "")
    return getattr(obj, attr_name, "")

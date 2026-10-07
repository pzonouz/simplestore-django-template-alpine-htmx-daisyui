# templatetags/persian_filters.py
from django import template

register = template.Library()

PERSIAN_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")


@register.filter(name="persianize")
def persianize(value):
    if value is None:
        return ""
    return str(value).translate(PERSIAN_DIGITS)

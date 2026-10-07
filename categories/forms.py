from django import forms
from django.core.exceptions import ValidationError

from .models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "parent", "description"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "input input-bordered w-full",
                    "placehoder": "نام",
                }
            ),
            "parent": forms.Select(attrs={"empty-label":"بدون والد","class": "select select-bordered w-full"}),
            "description": forms.Textarea(
                attrs={
                    "class": "input input-bordered w-full",
                    "rows": "2",
                    "placehoder": "توضیحات",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 1. Custom label for the root/null option
        self.fields["parent"].required = False
        self.fields["parent"].empty_label = "بدون والد"

        # 2. Queryset for parent choices (sorted)
        queryset = Category.objects.all().order_by("name")

        # 3. CRUCIAL for inline editing: Prevent circular reference
        # An existing category cannot be its own parent!
        if self.instance and self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)

        self.fields["parent"].queryset = queryset

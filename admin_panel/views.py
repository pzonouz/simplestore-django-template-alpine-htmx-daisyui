from django.shortcuts import render


def adminPanel(request):

    return render(request, "components/layouts/admin_layout.html")

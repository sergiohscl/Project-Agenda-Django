from django.shortcuts import render


def create(request):
    context = {

    }

    return render(
        request,
        'contact/create.html',
        context
    )

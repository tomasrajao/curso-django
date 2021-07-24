from django.shortcuts import render # noqa

# Create your views here.


def home(request):
    return render(request, 'base/home.html', {'contato_email': 'ramalho@python.pro.br'})

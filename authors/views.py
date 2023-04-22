from django.shortcuts import render
from authors.forms import RegisterForm


def register_view(request):
    if request.POST:
        form = RegisterForm(request.POST)
    else:
        form = RegisterForm()

    return render(request, 'authors/pages/register_view.html',
                  context={
                        'form': form
                  })

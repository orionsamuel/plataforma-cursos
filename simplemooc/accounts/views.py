from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL)
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/register.html', context)

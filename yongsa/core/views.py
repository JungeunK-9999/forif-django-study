from django.shortcuts import render, redirect
from core.form import HeroForm
import random


# Create your views here.
def home(request):
    return render(request, 'core/home.html')


def create_hero(request):
    if request.method == 'POST':
        form = HeroForm(request.POST)
        if form.is_valid():
            hero = form.save(commit=False)
            hero.atk = random.randint(50, 200)
            hero.save()

        return redirect('home')
    else:
        form = HeroForm()
    return render(request, 'core/create_hero.html', {'form': form})

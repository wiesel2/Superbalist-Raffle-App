from django.shortcuts import render
from .forms import homeForm
import random

names_list = []
def home(request):

    title = "Welcome to the raffle"
    description = "Enter names into the raffle and then click draw to view the winner!"
    form = homeForm(request.POST or None)

    context = {
        "title": title,
        "description": description,
        "form": form,

    }
    if form.is_valid():
        instance = form.cleaned_data.get("full_name")
        names_list.append(instance)

    print names_list



    return render(request, "home.html", context)

def winner(request):
    r = random.randint(0, (len(names_list)-1))
    winner_name = names_list[r]


    title = "The winner is:"
    context = {
        "title": title,
        "winner_name": winner_name

    }

    del names_list[:]
    return render(request, "winner.html", context)
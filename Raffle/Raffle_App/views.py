from django.shortcuts import render
from .forms import homeForm
import random

names_list = []
def home(request):

    title = "Welcome to the raffle"
    title2 = "Raffle"
    description = "Enter names into the raffle and then click draw to view the winner!"
    description2 = " has been added to the draw"
    description3 = "Enter another name or click draw to view the winner!"

    form = homeForm(request.POST or None)

    context = {
        "title": title,
        "description": description,
        "form": form,

    }
    if form.is_valid():
        instance = form.cleaned_data.get("full_name")
        names_list.append(instance)
        context = {
            "title2": title2,
            "description2": instance + description2,
            "description3": description3,
            "form": form,
        }

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
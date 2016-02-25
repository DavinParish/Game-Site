from django.http import request
from django.shortcuts import render
from .models import Score, Screenshot, User, Game
# Create your views here.


def detail(request, game_id=None):
    # make a list of screenshots for a specific game
    screenshots = Screenshot.objects.all()
    game = Game.objects.get(id=game_id)
    scores = Score.objects.filter(game=game).order_by('-score')[:5]

    context = {
        "screenshots": screenshots,
        "scores": scores,
        "game": game,
    }
    return render(request, 'scores/detail.html', context)



def base(request):

    # make a list of all games
    games = Game.objects.all()
    context = {
        "games": games,
    }
    return render(request, 'scores/base.html', context)

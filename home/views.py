from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import JsonResponse

from stockfish import Stockfish


class HomeView(View):

    template = 'home/main.html'

    def get(self, request):
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal
        }
        return render(request, self.template, context)

def play_back(fen):
    sf = Stockfish()
    sf.set_fen_position(fen)
    next_move = sf.get_best_move()
    return next_move

def game_answer(request):
    if request.method == "GET":
        fen = request.GET['fen']
        next_move = play_back(fen)
        context = {
            'from': next_move[:2],
            'to': next_move[2:]
        }
        return JsonResponse(context)

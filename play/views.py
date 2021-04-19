from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_exempt

from stockfish import Stockfish


@xframe_options_exempt
def board_view(request):
    if request.method == 'GET':
        print('--')
        print(request.GET)
        print('--')
        template_name = 'play/game.html'
        return render(request, template_name, {})

def play_back(fen):
    sf = Stockfish()
    sf.set_fen_position(fen)
    next_move = sf.get_best_move()
    del sf
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

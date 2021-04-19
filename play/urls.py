from django.urls import path

from .views import (
    board_view,
    game_answer
)


app_name = 'play'
urlpatterns = [
    path('', board_view, name='board'),
    path('playback', game_answer, name='back')
]

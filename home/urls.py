from django.urls import path

from .views import (
    HomeView,
    game_answer
)

app_name = 'home'
urlpatterns = [
    path('', HomeView.as_view(), name='page'),
    path('playback', game_answer, name='back')
]

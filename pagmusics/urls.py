from django.urls import path
from pagmusics.views import *

urlpatterns = [
    path('', index),
    path('axe_music/', axe_music),
    path('chill_vibes/', chill_vibes),
    path('city_pop/', city_pop),
    path('indie_rock/', indie_rock),
    path('jazz/', jazz),
    path('mpb/', mpb),
    path('rock/', rock),
    path('romantic/', romantic),
]
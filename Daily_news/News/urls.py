from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name='index'),
    path('',views.main_page,name='main_page'),
    path('business/',views.business,name='business'),
    path('sports/',views.sports,name='sports'),
    path('entertainment/',views.entertainment,name='entertainment'),
    path('technology/',views.technology,name='technology'),
    path('life_style/',views.life_style,name='life_style'),
    path('food/',views.food,name='food'),
    path('weather/',views.weather,name='weather'),
    path('eduaction/',views.education,name='education'),
    path('politics/',views.politics,name='politics'),
    path('world/',views.world,name='world'),
    path('pollution/',views.pollution,name='pollution'),
    path('animal/',views.animal,name='animal'),
    path('health/',views.health,name='health'),
    path('science/',views.science,name='science'),
    path('fashion/',views.fashion,name='fashion'),
    path('crime/',views.crime,name='crime'),
    path('bollywood/',views.bollywood,name='bollywood'),
    path('hollywood/',views.hollywood,name='hollywood'),
    path('tollywood/',views.tollywood,name='tollywood'),
    path('games/',views.games,name='games'),
    path('students/',views.students,name='students'),
]
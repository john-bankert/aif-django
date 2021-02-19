from django.urls import path, re_path
from . import views
from .views import IndexView, CharacterView  # , CharacterViewEx

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('logout', views.logouts, name='logout'),
    path('load-character-sheet/', views.load_character_sheet, name='load_character_sheet'),
    path('edit-character-sheet/', views.edit_character_sheet, name='edit_character_sheet'),
    path('character/<str:char_name>/', CharacterView.as_view(), name='character'),
    # path('<str:char_name>/edit', views.edit, name='edit'),
    # path('<str:char_name>/save', views.save, name='save'),
    # path('character/<str:char_name>/', views.character, name='character'),
    # path('ajax-set-theme/', views.set_theme, name='set_theme'),
    # path('menu/<str:option>/', views.menu, name='menu'),
    # path('accounts/sign_up/', views.sign_up, name="sign-up"),
    # path('<str:char_name>/sheet', views.sheet, name='sheet'),
]
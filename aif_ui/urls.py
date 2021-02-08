from django.urls import path, re_path
from . import views
from .views import IndexView, CharacterView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('logout', views.logouts, name='logout'),
    path('character/<str:char_name>/', CharacterView.as_view(), name='character'),
    # path('character/<str:char_name>/', views.character, name='character'),
    # path('', views.index, name='index'),
    # path('ajax-set-theme/', views.set_theme, name='set_theme'),
    # path('menu/<str:option>/', views.menu, name='menu'),
    # path('<str:char_name>/save', views.save, name='save'),
    # path('accounts/sign_up/', views.sign_up, name="sign-up"),
    # path('<str:char_name>/', views.sheet, name='sheet'),
    # path('<str:char_name>/sheet', views.sheet, name='sheet'),
    # path('<str:char_name>/edit', views.edit, name='edit'),
]
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('index2', views.index2, name='index2'),
    path('logout', views.logouts, name='logout'),
    path('character/<str:char_name>/', views.character, name='character'),
    path('menu/<str:option>/', views.menu, name='menu'),
    path('ajax-set-theme/', views.set_theme, name='set_theme'),
    # path('accounts/sign_up/', views.sign_up, name="sign-up"),
    # path('<str:char_name>/', views.sheet, name='sheet'),
    # path('<str:char_name>/sheet', views.sheet, name='sheet'),
    # path('<str:char_name>/edit', views.edit, name='edit'),
    path('<str:char_name>/save', views.save, name='save'),
]
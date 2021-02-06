from django.urls import path, re_path
from . import views
from .views import MyView, IndexView

urlpatterns = [
    # path('', views.index, name='index'),
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index-view'),
    path('logout', views.logouts, name='logout'),
    path('character/<str:char_name>/', views.character, name='character'),
    path('menu/<str:option>/', views.menu, name='menu'),
    path('ajax-set-theme/', views.set_theme, name='set_theme'),
    path('<str:char_name>/save', views.save, name='save'),
    path('mine/', MyView.as_view(), name='my-view'),
    path('index/', IndexView.as_view(), name='index-view'),
    # path('accounts/sign_up/', views.sign_up, name="sign-up"),
    # path('<str:char_name>/', views.sheet, name='sheet'),
    # path('<str:char_name>/sheet', views.sheet, name='sheet'),
    # path('<str:char_name>/edit', views.edit, name='edit'),
]
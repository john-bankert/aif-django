from django.shortcuts import get_object_or_404, render, HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from aif_character.models import Character, CharacterForm
from aif_ui.models import Themes


def index(request):
    context = {'flag': 'index', 'themes': Themes.objects.filter(name)}
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
    if request.user.is_authenticated:
        fc = Character.objects.filter(player=request.user.username, open=True)
        context['fc'] = fc
    print(context)
    return render(request, 'aif_ui/index.html', context)


def logouts(request):
    logout(request)
    # context = {'flag': 'index'}
    # if request.user.is_authenticated:
    #    fc = Character.objects.filter(player=request.user.username, open=True)
    #    context['fc'] = fc
    return index(request)


def menu(request, option):
    context = {'flag': 'index'}
    print("option = " + option)
    return render(request, 'aif_ui/index.html', context)


def character(request, char_name):
    context = {'flag': 'sheet', 'character': get_object_or_404(Character, name=char_name)}
    if request.user.is_authenticated:
        fc = Character.objects.filter(player=request.user.username, open=True)
        context['fc'] = fc
    # c = context['character']
    # if c:
    #    if c.skills_set.all():
    #        for s in c.skills_set.all():
    #            print(s.skill_type, s.name,  s.sort_order)
    return render(request, 'aif_ui/index.html', context)


def edit(request, char_name):
    context = {'flag': 'edit', 'character': get_object_or_404(Character, name=char_name)}
    return render(request, 'aif_ui/sheet.html', context)


def save(request, char_name):
    char = Character.objects.get(name=char_name)
    char_form = CharacterForm(request.POST, instance=char)
    char_form.save()

    for skill in char.classskills_set.all():
        skill.rank = int(request.POST.get(skill.item_name + "_rank"))
        skill.save()

    for skill in char.racialskills_set.all():
        skill.rank = int(request.POST.get(skill.item_name + "_rank"))
        skill.save()

    if "Paladin" in char.char_class:
        for skill in char.honorskills_set.all():
            skill.rank = int(request.POST.get(skill.item_name + "_rank"))
            skill.save()

    context = {'flag': 'edit', 'character': char}
    return render(request, 'aif_ui/sheet.html', context)


def set_theme(request):
    themes = {'black': {'c1': 'black', 'c2': 'white', 'c3': 'silver', 'c4': 'black', 'c5': 'white'},
              'blue': {'c1': 'navy', 'c2': 'dodgerblue', 'c3': 'dodgerblue', 'c4': 'black', 'c5': 'white'},
              'brown': {'c1': 'saddlebrown', 'c2': 'yellow', 'c3': 'yellow', 'c4': 'black', 'c5': 'white'},
              'green': {'c1': 'darkgreen', 'c2': 'lime', 'c3': 'lime', 'c4': 'black', 'c5': 'white'},
              'orange': {'c1': 'darkorange', 'c2': 'gold', 'c3': 'gold', 'c4': 'black', 'c5': 'white'},
              'red': {'c1': 'darkred', 'c2': 'red', 'c3': 'red', 'c4': 'black', 'c5': 'white'},
              }

    text = request.POST['theme']
    theme = themes[text]
    if request.user.is_authenticated:
        print('pre', request.user.profile.navbar_bg_color)
        request.user.profile.navbar_bg_color = theme['c1']
        request.user.profile.menubar_bg_color = theme['c2']
        request.user.profile.tabbar_hover_bg_color = theme['c3']
        request.user.profile.tabbar_hover_fg_color = theme['c4']
        request.user.profile.tabbar_active_bg_color = theme['c1']
        request.user.profile.tabbar_active_fg_color = theme['c5']
        request.user.profile.save()
        print('post', request.user.profile.navbar_bg_color)
    response = text + ":)"
    # Send the response

    return HttpResponse(response)

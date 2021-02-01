from django.shortcuts import get_object_or_404, render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from aif_character.models import Character, CharacterForm


def index(request):
    context = {'flag': 'index'}
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



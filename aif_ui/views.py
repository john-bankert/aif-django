from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.views import View
from django.views.generic.base import TemplateView

from aif_character.models import Character, CharacterForm
from aif_ui.models import Themes


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


class IndexView(TemplateView):

    template_name = "aif_ui/index.html"

    def __init__(self):
        # class copy of request so it can be accessed in get_context_data method
        self.request = None

    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('post')
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
        # return render(request, "index.html")

    def http_method_not_allowed(self, request, *args, **kwargs):
        print('http_method_not_allowed')
        return super().http_method_not_allowed(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        print('get_context_data')
        context = super().get_context_data(**kwargs)
        context['flag'] = 'index'
        if self.request.user.is_authenticated:
            context['fc'] = Character.objects.filter(player=self.request.user.username, open=True)
        return context


def index(request):
    context = {'flag': 'index'}
    # t = Themes.objects.all()
    # for t in Themes.objects.all():
    #    _themes.append(t.name)
    # context['themes'] = t
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
    return render(request, 'aif_ui/index.html', context)


def logouts(request):
    logout(request)
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
    # for key in request.GET:
    #    print(key, request.GET[key])
    # for key in request.POST:
    #    print(key, request.POST[key])
    request.user.session.current_tab = request.POST['tab_name']
    request.user.session.save()
    response = ":)"
    return HttpResponse(response)

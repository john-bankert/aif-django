from django.shortcuts import get_object_or_404, render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic.base import TemplateView
from aif_character.models import Character, CharacterForm
from aif_ui.models import Themes

global_character_name = ""
global_theme_name = ""


class IndexView(TemplateView):

    template_name = "aif_ui/index.html"

    def __init__(self):
        self.request = None

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'theme_selected' in request.POST:  # POST from theme selector modal
            global global_theme_name
            global_theme_name = request.POST['theme_selected']
            Themes.add_to_user(request)
            return HttpResponseRedirect('.')
        elif 'username' in request.POST:  # POST from login modal
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    self.request = request
                    return HttpResponseRedirect('/')
                else:
                    self.request = request
                    return HttpResponse("Inactive user.")
            else:
                self.request = request
                return HttpResponseRedirect('/')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flag'] = 'index'
        context['themes'] = Themes.objects.all()
        context['character'] = get_object_or_404(Character, name=global_character_name)
        context['current_theme'] = global_theme_name
        if self.request.user.is_authenticated:
            context['fc'] = Character.objects.filter(player=self.request.user.username, open=True)
        return context


class CharacterView(TemplateView):

    template_name = "aif_ui/index.html"

    def __init__(self):
        self.request = None

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if 'theme_selected' in request.POST:
            self.request = request
            global global_theme_name
            global_theme_name = request.POST['theme_selected']
            Themes.add_to_user(request)
            return HttpResponseRedirect('.')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global global_character_name
        global_character_name = context['char_name']
        context['flag'] = 'character'
        context['character'] = get_object_or_404(Character, name=global_character_name)
        context['current_theme'] = global_theme_name
        context['themes'] = Themes.objects.all()
        if self.request.user.is_authenticated:
            context['fc'] = Character.objects.filter(player=self.request.user.username, open=True)
        return context


def logouts(request):
    logout(request)
    return HttpResponseRedirect('/')


'''

def character(request, char_name):
    context = {'flag': 'sheet', 'character': get_object_or_404(Character, name=char_name)}
    print(context)
    if request.user.is_authenticated:
        fc = Character.objects.filter(player=request.user.username, open=True)
        context['fc'] = fc
    return HttpResponseRedirect('/', [], context)
    # return render(request, 'aif_ui/index.html', context)

def save(request, char_name):
    char = Character.objects.get(name=char_name)
    char_form = CharacterForm(request.POST, instance=char)
    char_form.save()

    for skill in char.classskills_set.all():
        skill.rank = int(request.POST.get(skill.name + "_rank"))
        skill.save()

    for skill in char.racialskills_set.all():
        skill.rank = int(request.POST.get(skill.name + "_rank"))
        skill.save()

    if "Paladin" in char.char_class:
        for skill in char.honorskills_set.all():
            skill.rank = int(request.POST.get(skill.name + "_rank"))
            skill.save()

    context = {'flag': 'edit', 'character': char}
    return render(request, 'aif_ui/sheet.html', context)
    
def edit(request, char_name):
    context = {'flag': 'edit', 'character': get_object_or_404(Character, name=char_name)}
    return render(request, 'aif_ui/sheet.html', context)

# example views function for using ajax
def set_theme(request):
    # for key in request.GET:
    #    print(key, request.GET[key])
    # for key in request.POST:
    #    print(key, request.POST[key])
    request.user.session.current_tab = request.POST['tab_name']
    request.user.session.save()
    response = ":)"
    return HttpResponse(response)


def menu(request, option):
    context = {'flag': 'index'}
    print("option = " + option)
    return render(request, 'aif_ui/index.html', context)


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
    
    # example using ajax 
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
    <script>
    function setTheme() {
        var x = document.getElementById("set_theme").value;
        $.ajax({
            type: "POST",
            url: '{{ '/ajax-set-theme/' }}',
            data: { csrfmiddlewaretoken: '{{ csrf_token }}', theme: x },
            success: function callback(response){
                       /* do whatever with the response */
                        document.getElementById("theme_popup").style.display = "none";
                       //alert(response);
                    }
        });
        location.reload();
    }
    </script>    
        
'''
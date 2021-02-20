from django.shortcuts import get_object_or_404, render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic.base import TemplateView
from aif_character.models import Character, CharacterForm
from aif_ui.models import Themes

global_character_name = ""
global_sheet_id = ""
global_theme_name = ""


class IndexView(TemplateView):

    template_name = "aif_ui/index.html"

    def __init__(self):
        self.request = None

    def dispatch(self, request, *args, **kwargs):
        print('IndexView.dispatch')
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('IndexView.post')
        if 'theme_selected' in request.POST:  # POST from theme selector modal
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
        elif 'char_to_open' in request.POST:
            return HttpResponseRedirect('/character/' + request.POST['char_to_open'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flag'] = 'index'
        context['sheet_id'] = 'sheet_1'
        context['current_theme'] = 'black'
        context['themes'] = Themes.objects.all().values('name')
        if self.request.user.is_authenticated:
            if self.request.user.session.character_name:
                context['character'] = get_object_or_404(Character, name=self.request.user.session.character_name)
            if self.request.user.session.current_theme:
                context['current_theme'] = self.request.user.session.current_theme
            context['fc'] = Character.objects.filter(player=self.request.user.username, open=True)\
                .values('name', 'char_class')
            self.request.user.session.ui_state = context['flag']
            self.request.user.session.sheet_id = context['sheet_id']
            self.request.user.session.save()
        context['sheet_url'] = 'aif_character/' + context['sheet_id'].strip() + '.html'
        return context


class CharacterView(TemplateView):

    template_name = "aif_ui/index.html"

    def __init__(self):
        self.request = None

    def dispatch(self, request, *args, **kwargs):
        print('CharacterView dispatch')
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('CharacterView post')
        if 'theme_selected' in request.POST:
            Themes.add_to_user(request)
            return HttpResponseRedirect('.')
        elif 'char_to_open' in request.POST:
            self.request.user.session.character_name = request.POST['char_to_open']
            self.request.user.session.save()
            return HttpResponseRedirect('/character/' + request.POST['char_to_open'])
        else:
            return HttpResponseRedirect(".")

    def get_context_data(self, **kwargs):
        print('CharacterView get_context_data')
        context = super().get_context_data(**kwargs)
        context['flag'] = 'character'
        context['sheet_id'] = 'sheet_1'
        context['current_theme'] = 'black'
        context['themes'] = Themes.objects.all().values('name')
        if self.request.user.is_authenticated:
            if self.request.user.session.character_name:
                context['character'] = get_object_or_404(Character, name=self.request.user.session.character_name)
            if self.request.user.session.current_theme:
                context['current_theme'] = self.request.user.session.current_theme
            context['fc'] = Character.objects.filter(player=self.request.user.username, open=True)\
                .values('name', 'char_class')
            self.request.user.session.ui_state = context['flag']
            self.request.user.session.sheet_id = context['sheet_id']
            self.request.user.session.save()
        context['sheet_url'] = 'aif_character/' + context['sheet_id'].strip() + '.html'
        return context


def logouts(request):
    logout(request)
    return HttpResponseRedirect('/')


# example views function for using ajax
def load_character_sheet(request):
    if request.method == 'POST':
        print('load character sheet')
        for key in request.POST:
            print(key, request.POST[key])
        context = {'flag': 'character', 'sheet_id': request.POST['sheet_id'],
                   'current_theme': request.POST['current_theme'], 'themes': Themes.objects.all()}
        if Character.objects.filter(name=request.POST['character_name']):
            context['character'] = get_object_or_404(Character, name=request.POST['character_name'])
        if request.user.is_authenticated:
            context['fc'] = Character.objects.filter(player=request.user.username, open=True)
        context['sheet_url'] = 'aif_character/' + request.POST['sheet_id'] + '.html'
        request.user.session.current_tab = request.POST['sheet_id']
        request.user.session.save()
        print(context)
        return render(request, context['sheet_url'], context)
    
    
# example views function for using ajax
def edit_character_sheet(request):
    if request.method == 'POST':
        print('edit character sheet')
        for key in request.POST:
            print(key, request.POST[key])
        context = {'flag': request.POST['flag'], 'sheet_id': request.POST['sheet_id'],
                   'current_theme': request.POST['current_theme'], 'themes': Themes.objects.all()}
        if Character.objects.filter(name=request.POST['character_name']):
            context['character'] = get_object_or_404(Character, name=request.POST['character_name'])
        if request.user.is_authenticated:
            context['fc'] = Character.objects.filter(player=request.user.username, open=True)
        context['sheet_url'] = 'aif_character/' + request.POST['sheet_id'] + '.html'
        request.user.session.current_tab = request.POST['sheet_id']
        request.user.session.save()
        return render(request, 'aif_ui/body_blow.html', context)


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


    {% load cache_bust %}

    <link rel="stylesheet" href="{% static "css/project.css" %}?{% cache_bust %}"/>    
        
'''
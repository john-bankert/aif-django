from django.shortcuts import get_object_or_404, render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.views.generic.base import TemplateView
from aif_character.models import Character, CharacterForm, CharacterForm2
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
        print('cv.dispatch')
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('cv.post')
        if 'theme_selected' in request.POST:
            Themes.add_to_user(request)
            return HttpResponseRedirect('.')
        elif 'char_to_open' in request.POST:
            request.user.session.character_name = request.POST['char_to_open']
            request.user.session.sheet_id = 'Sheet_1'
            request.user.session.save()
            return HttpResponseRedirect('/character/' + request.POST['char_to_open'])
        elif 'save_character' in request.POST:
            request.user.session.ui_state = 'character'
            request.user.session.save()
            print('saving character')
            # for key in request.POST:
            #    print(key, request.POST[key])

            char = Character.objects.get(name=request.user.session.character_name)
            if request.user.session.sheet_id == 'Sheet_3' or request.user.session.sheet_id == 'Sheet_4':
                char_form = CharacterForm2(request.POST, instance=char)
            else:
                char_form = CharacterForm(request.POST, instance=char)
            char_form.save()

            for skill in char.skills_set.all():
                skill.rank = int(request.POST.get(skill.name + "_rank"))
                skill.save()
            print("sheet id =",request.user.session.sheet_id)
            # return HttpResponseRedirect('/character/' + request.user.session.character_name)
            # return HttpResponseRedirect(".")
            context = {'flag': request.user.session.ui_state, 'sheet_id': request.user.session.sheet_id,
                       'current_theme': request.user.session.current_theme, 'themes': Themes.objects.all()}
            if Character.objects.filter(name=request.user.session.character_name):
                context['character'] = get_object_or_404(Character, name=request.user.session.character_name)
            if request.user.is_authenticated:
                context['fc'] = Character.objects.filter(player=request.user.username, open=True)
            return render(request, 'aif_character/' + request.user.session.sheet_id + '.html', context)
        else:
            return HttpResponseRedirect(".")

    def get_context_data(self, **kwargs):
        print('cv.get_context')
        context = super().get_context_data(**kwargs)
        context['flag'] = 'character'
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
            self.request.user.session.save()
        context['sheet_url'] = 'aif_character/' + self.request.user.session.sheet_id.strip() + '.html'
        return context


def logouts(request):
    logout(request)
    return HttpResponseRedirect('/')


# example views function for using ajax
def load_character_sheet(request):
    if request.method == 'POST':
        request.user.session.sheet_id = request.POST['sheet_id']
        request.user.session.save()
        print('session.sheet_id', request.user.session.sheet_id)
        print('session.character_name', request.user.session.character_name)
        print('session.ui_state', request.user.session.ui_state)
        print('session.current_theme', request.user.session.current_theme)
        context = {'flag': request.user.session.ui_state, 'sheet_id': request.user.session.sheet_id,
                   'current_theme': request.user.session.current_theme, 'themes': Themes.objects.all()}
        if Character.objects.filter(name=request.user.session.character_name):
            context['character'] = get_object_or_404(Character, name=request.user.session.character_name)
        if request.user.is_authenticated:
            context['fc'] = Character.objects.filter(player=request.user.username, open=True)
        print('sheet url', 'aif_character/' + request.user.session.sheet_id + '.html')
        return render(request, 'aif_character/' + request.user.session.sheet_id + '.html', context)
    
    
# example views function for using ajax
def edit_character_sheet(request):
    if request.method == 'POST':
        request.user.session.ui_state = 'edit'
        request.user.session.save()
        print('session.sheet_id', request.user.session.sheet_id)
        print('session.character_name', request.user.session.character_name)
        print('session.ui_state', request.user.session.ui_state)
        print('session.current_theme', request.user.session.current_theme)
        context = {'flag': 'edit', 'sheet_id': request.user.session.sheet_id,
                   'current_theme': request.user.session.current_theme, 'themes': Themes.objects.all()}
        if Character.objects.filter(name=request.user.session.character_name):
            context['character'] = get_object_or_404(Character, name=request.user.session.character_name)
        if request.user.is_authenticated:
            context['fc'] = Character.objects.filter(player=request.user.username, open=True)
        context['sheet_url'] = 'aif_character/' + context['sheet_id'].strip() + '.html'
        return render(request, context['sheet_url'], context)


'''

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
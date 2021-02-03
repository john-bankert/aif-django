from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def set_theme(user_name, theme_name):

    try:
        user = User.ojbects.get(username=user_name)
        if theme_name == 'black':
            user.profile.navbar_bg_color = 'black'
            user.profile.menubar_bg_color = 'white'
            user.profile.tabbar_hover_bg_color = 'silver'
            user.profile.tabbar_hover_fg_color = 'black'
            user.profile.tabbar_active_bg_color = 'black'
            user.profile.tabbar_active_fg_color = 'white'
        elif theme_name == 'blue':
            user.profile.navbar_bg_color = 'navy'
            user.profile.menubar_bg_color = 'dodgerblue'
            user.profile.tabbar_hover_bg_color = 'dodgerblue'
            user.profile.tabbar_hover_fg_color = 'black'
            user.profile.tabbar_active_bg_color = 'navy'
            user.profile.tabbar_active_fg_color = 'white'
        elif theme_name == 'brown':
            user.profile.navbar_bg_color = 'saddlebrown'
            user.profile.menubar_bg_color = 'yellow'
            user.profile.tabbar_hover_bg_color = 'yellow'
            user.profile.tabbar_hover_fg_color = 'black'
            user.profile.tabbar_active_bg_color = 'saddlebrown'
            user.profile.tabbar_active_fg_color = 'white'
        elif theme_name == 'green':
            user.profile.navbar_bg_color = 'darkgreen'
            user.profile.menubar_bg_color = 'lime'
            user.profile.tabbar_hover_bg_color = 'lime'
            user.profile.tabbar_hover_fg_color = 'black'
            user.profile.tabbar_active_bg_color = 'darkgreen'
            user.profile.tabbar_active_fg_color = 'white'
        elif theme_name == 'orange':
            user.profile.navbar_bg_color = 'darkorange'
            user.profile.menubar_bg_color = 'coral'
            user.profile.tabbar_hover_bg_color = 'coral'
            user.profile.tabbar_hover_fg_color = 'black'
            user.profile.tabbar_active_bg_color = 'darkorange'
            user.profile.tabbar_active_fg_color = 'white'
        elif theme_name == 'red':
            user.profile.navbar_bg_color = 'darkred'
            user.profile.menubar_bg_color = 'red'
            user.profile.tabbar_hover_bg_color = 'red'
            user.profile.tabbar_hover_fg_color = 'black'
            user.profile.tabbar_active_bg_color = 'darkred'
            user.profile.tabbar_active_fg_color = 'white'
        else:
            print('theme does not exist')
        user.profile.save()
    except ObjectDoesNotExist:
        print(user_name, "does not exist")

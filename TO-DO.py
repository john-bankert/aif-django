'''
https://help.dreamhost.com/hc/en-us/articles/360002341572-Creating-a-Django-project
https://developer.mozilla.org/en-US/docs/Web/CSS/--*
https://blog.jim-nielsen.com/2019/generating-shades-of-color-using-css-variables/
https://lincolnloop.com/blog/user-generated-themes-django-css/
https://github.com/lethain/django-userskins
https://levelup.gitconnected.com/how-to-implement-login-logout-and-registration-with-djangos-user-model-59442164db73
https://www.w3schools.com/howto/howto_js_sticky_header.asp
https://www.w3schools.com/howto/howto_js_tabs.asp
https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/button
https://stackoverflow.com/questions/15341285/how-do-i-call-a-django-function-on-button-click
https://stackoverflow.com/questions/32347383/create-a-popup-login-register-page-using-django
https://stackoverflow.com/questions/37982412/django-login-from-in-modal-window
https://stackoverflow.com/questions/2412770/good-ways-to-sort-a-queryset-django
https://docs.djangoproject.com/en/3.1/topics/serialization/
https://docs.djangoproject.com/en/3.1/ref/forms/widgets/
https://stackoverflow.com/questions/7302889/textfield-missing-in-django-forms
https://www.codingforentrepreneurs.com/blog/html-template-to-pdf-in-django
https://stackoverflow.com/questions/1377446/render-html-to-pdf-in-django-site
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
https://stackoverflow.com/questions/51106830/how-to-call-python-functions-from-javascript-in-django

######################################

 questions for Matt:

 can crossbows use different quarrel types: eg small cb use medium quarrel, large cb use small or medium quarrel, etc
 crossbow skill - is using medium translatable to large or small, for example?
 illusionist - # cards per circle is 1 + affinity rank? or just affinity rank. Couldn't find it explicitly
               stated in rules.

######################################

 Conversion Tasks
 Armor, Equipement, Weapons - need to preserver indenting and sorting from PDF tables
                            - when adding to character, ammo needs to go into equipment
                              not weapons list
 Separate out weapons/armor skills tracking (rank, order) from actual weapons/armor lists
 normalize field names: eg item_name/name, adjusted -> display, etc.
 Sorting index to allow for custom sorting of anything list based?
 Sorting of query sets where appropriate
 refactor table names Armor, Equipment, etc in either Character or PlayersTome so they're not identical
 duplicate container names allowed?
 Preference should include: base font, base font size, and colors.
 class based views/forms
 Formulas of some sort for buffs, etc.
 multiclass of bard/priest or similar correctly showing spell/rhythm/etc
 Something may be missing in the linking between certain things. Not 100% sure just yet
 select option light blue color change if possible. UL,LI instead of select?
 TODO - HIGH
 new combat/close combat need to do something to adjust buff round start/end across multiple combats
 Speed debuff on expiration
 track ability use per day where applicable
 try and narrow things up to fit combat tab in whole in tablet mode
 notes are not being saved
 Separate Knockback DEX check roll field on combat tab - balance
 all extra dice from weapon go to attack, not split between attack and damage

 TODO - MEDIUM
 print/generate PDF
 equipment buff list
 XP Change - check to see if new level, bump up level and do other things such as 
             reminder about skill points, rank up mastered skills, skill up, etc.
 Skill Mastery - in weapons, need some method to deal with stuff like Pike +2, Yawp +4
                 should track by Pike, or multiple entries for same weapon with diff props
                 such as Hand Axe, Hand Axe +2 - track by Hand Axe only.
 Skill Mastery - in armor, need to filter out (or show as mastered if applicable) entries such as
                 Toughness (for Dwarves) or Protection Spell (for Wizards)
 Enhanced combat simulator to test things as they're added
 validation on edit where necessary - can't lower XP, etc.
 Change equipment to work like skills, weapons and armor. Have a list for each container.
 Equipment should check container content load vs container content capacity
 protection spell is in armor for dingle. does it belong there or somewhere else?
 formatting of calculated load values - doubles should be max two decimals
 Fatigue recovery rate displayed somewhere.
 Mods do not stack - highest mod only applies.
 Extract out buffs and stuff into XML files so not need to update code?
 Containers in equipment

 TODO - LOW
 change edit day/time from popup to in-line on the display label, if possible.
 Rename character
 add new multiclass
 fancy dice roller
 weapons/armor/equip catalogs - add/delete/buy from each.
 label popup needs to adjust for scroll position, etc.

######################################
 
'''


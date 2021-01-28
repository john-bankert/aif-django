from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist


class Command(BaseCommand):


    def add_arguments(self, parser):
        pass
        
    def handle(self, *args, **options):
        self.add_users()

    def add_users(self):
        self.add_user('John', 'jbankert@gmail.com', 'k72CD@&rsa49PKF', 'John', 'Bankert')
        self.add_user('demo', 'demo@aif.magichelmet.xyz', '1qaz2wsx!QAZ@WSX', 'Demo', 'User')
        self.add_user('Gamemaster', 'gamemaster@aif.magichelmet.xyz', '1234qwer!@#$QWER', 'Game', 'Masater')
        # new_group, created = Group.objects.get_or_create(name='game_master')
        # proj_add_perm = Permission.objects.get(name='Can add users to party')
        # new_group.permissions.add(proj_add_perm)
        # ct = ContentType.objects.get_for_model(Project)
        # permission = Permission.objects.create(codename='can_add_project', name='Can add project', content_type=ct)
        # new_group.permissions.add(permission)
        # new_group, created = Group.objects.get_or_create(name='aif_admin')

    def add_user(self, userName, email, password, firstName, lastName,):
        if User.objects.filter(username=userName).count() == 0:
            user = User.objects.create_user(userName, email, password)
            user.first_name = firstName
            user.last_name = lastName
            user.save()
            self.stdout.write("added user " + userName)
        else:
            self.stdout.write("user " + userName + " already exists")


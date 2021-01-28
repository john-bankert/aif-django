import sys, os
INTERP = "/home/bankertj531/aif.magichelmet.xyz/venv/bin/python3"
# INTERP is present twice so that the new python interpreter
# knows the actual executeable path
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/aif')

sys.path.insert(0, cwd + '/venv/bin')
sys.path.insert(0, cwd + '/venv/lib/python3.9/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = "aif.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
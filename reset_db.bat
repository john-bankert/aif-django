del aif_character\migrations\0*.py
del aif_playerstome\migrations\0*.py
del db.sqlite3
python manage.py makemigrations aif_character
python manage.py makemigrations aif_playerstome
python manage.py migrate
set DJANGO_SUPERUSER_PASSWORD=z89SU$$jpz98AER
set DJANGO_SUPERUSER_EMAIL=admin@example.com
python manage.py createsuperuser --username=admin --no-input
python manage.py createdemodata
python manage.py ptimport
python manage.py create_characters
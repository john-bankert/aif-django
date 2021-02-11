# Generated by Django 3.1.2 on 2021-02-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArmorCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=150)),
                ('category', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=100)),
                ('cost', models.CharField(default='', max_length=15)),
                ('type', models.CharField(default='', max_length=5)),
                ('slashing', models.CharField(default='', max_length=5)),
                ('piercing', models.CharField(default='', max_length=5)),
                ('bludgeoning', models.CharField(default='', max_length=5)),
                ('cleaving', models.CharField(default='', max_length=5)),
                ('load', models.CharField(default='', max_length=10)),
                ('carried', models.CharField(default='', max_length=10)),
                ('durability', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=150)),
                ('category', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=100)),
                ('cost', models.CharField(default='', max_length=15)),
                ('load', models.CharField(default='', max_length=10)),
                ('capacity', models.CharField(default='', max_length=10)),
                ('slashing', models.CharField(default='', max_length=5)),
                ('piercing', models.CharField(default='', max_length=5)),
                ('bludgeoning', models.CharField(default='', max_length=5)),
                ('cleaving', models.CharField(default='', max_length=5)),
                ('durability', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SkillsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=150)),
                ('name', models.CharField(default='', max_length=100)),
                ('skill_type', models.CharField(default='', max_length=10)),
                ('skill_class', models.CharField(default='', max_length=25)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SpellsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=150)),
                ('category', models.CharField(default='', max_length=50)),
                ('circle', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=100)),
                ('area', models.CharField(default='', max_length=50)),
                ('duration', models.CharField(default='', max_length=50)),
                ('range', models.CharField(default='', max_length=50)),
                ('saves', models.CharField(default='', max_length=50)),
                ('upkeep', models.CharField(default='', max_length=10)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WeaponsCatalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(default='', max_length=150)),
                ('category', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=100)),
                ('cost', models.CharField(default='', max_length=15)),
                ('size', models.CharField(default='', max_length=5)),
                ('type', models.CharField(default='', max_length=5)),
                ('damage', models.CharField(default='', max_length=15)),
                ('range', models.CharField(default='', max_length=15)),
                ('load', models.CharField(default='', max_length=10)),
                ('durability', models.CharField(default='', max_length=10)),
            ],
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-01 11:52

from django.db import migrations

default_settings = [('Current Game', 'Pokemon Ultra Sun'),
                    ('Current Run', '(default)'),
                    ('Quotee', 'Someone'),
                    ('Cooldown Seconds', '10'),
                    ('IRC Service', 'Running'),
                    ('Twitch Username', ''),
                   ]

def create_default_settings(apps, schema_editor):
    Setting = apps.get_model('dashboard', 'Setting')

    setting_objects = []
    for setting in default_settings:
        setting_object = Setting(key=setting[0], value=setting[1])
        setting_objects.append(setting_object)

    Setting.objects.bulk_create(setting_objects)

class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_setting'),
    ]

    operations = [
        migrations.RunPython(create_default_settings),
    ]

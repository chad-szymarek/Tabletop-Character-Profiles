# Generated by Django 4.0.3 on 2022-04-06 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_charactergoallist_charactergoal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='goals',
        ),
        migrations.RemoveField(
            model_name='character',
            name='goalscomplete',
        ),
    ]

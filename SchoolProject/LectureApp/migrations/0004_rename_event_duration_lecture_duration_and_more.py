# Generated by Django 4.0.1 on 2022-01-25 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LectureApp', '0003_remove_lecture_quantity_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lecture',
            old_name='event_duration',
            new_name='duration',
        ),
        migrations.RenameField(
            model_name='lecture',
            old_name='event_form',
            new_name='form',
        ),
    ]

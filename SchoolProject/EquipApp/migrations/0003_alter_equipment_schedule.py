# Generated by Django 4.0.1 on 2022-01-25 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EquipApp', '0002_alter_equipment_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='schedule',
            field=models.JSONField(blank=True, default=dict, verbose_name='Расписание'),
        ),
    ]
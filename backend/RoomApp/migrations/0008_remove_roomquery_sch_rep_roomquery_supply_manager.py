# Generated by Django 4.1.3 on 2023-02-02 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_schrep_credential_id_supplymanager'),
        ('RoomApp', '0007_alter_roombooking_contract'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomquery',
            name='sch_rep',
        ),
        migrations.AddField(
            model_name='roomquery',
            name='supply_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.supplymanager', verbose_name='Завхоз'),
        ),
    ]

# Generated by Django 4.1.3 on 2023-02-02 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_schrep_credential_id_supplymanager'),
        ('EquipApp', '0013_alter_equipquery_sch_rep'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipquery',
            name='sch_rep',
        ),
        migrations.AddField(
            model_name='equipquery',
            name='supply_manager',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.supplymanager', verbose_name='Представитель'),
            preserve_default=False,
        ),
    ]

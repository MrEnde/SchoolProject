# Generated by Django 4.1.3 on 2023-01-24 22:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_schoolrepresentative_remove_schrep_school_and_more'),
        ('RoomApp', '0006_alter_roomquery_sch_rep'),
        ('EquipApp', '0013_alter_equipquery_sch_rep'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.DeleteModel(
            name='SchRep',
        ),
        migrations.AddField(
            model_name='schoolrepresentative',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.school'),
        ),
        migrations.AddField(
            model_name='schoolrepresentative',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

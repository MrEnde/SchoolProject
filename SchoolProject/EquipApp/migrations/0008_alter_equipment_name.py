# Generated by Django 4.0.1 on 2022-01-25 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EquipApp', '0007_alter_equipment_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
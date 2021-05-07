# Generated by Django 2.2.10 on 2021-05-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210507_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prog_entre',
            name='department_name',
        ),
        migrations.AlterField(
            model_name='prog_entre',
            name='program_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='prog_entre',
            name='program_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

# Generated by Django 4.1.3 on 2023-05-14 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0003_auto_20230501_1850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='first_lesson',
            field=models.CharField(blank=True, default='—', max_length=20, null=True, verbose_name='Первый урок'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

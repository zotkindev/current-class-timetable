# Generated by Django 3.1 on 2023-05-17 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetables', '0004_alter_category_id_alter_timetable_first_lesson_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

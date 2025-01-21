from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    name = models.CharField(max_length = 3, verbose_name = 'Класс')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.name
    class Meta: 
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'



class Timetable(models.Model):
    class_init = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = 'Класс')

    first_lesson = models.CharField('Первый урок', max_length = 20, default='—', null=True, blank=True)
    first_cabinet = models.CharField('Первый кабинет', max_length = 10, default='—', null = True, blank = True)

    second_lesson = models.CharField('Второй урок', max_length = 15, default='—', null=True, blank=True)
    second_cabinet = models.CharField('Второй кабинет', max_length = 10, default='—', null = True, blank = True)

    third_lesson = models.CharField('Третий урок', max_length = 15, default='—', null=True, blank=True)
    third_cabinet = models.CharField('Третий кабинет', max_length = 10, default='—', null = True, blank = True)

    fourth_lesson = models.CharField('Четвёртый урок', max_length = 15, default='—', null=True, blank=True)
    fourth_cabinet = models.CharField('Четвёртый кабинет', max_length = 10, default='—', null = True, blank = True)

    fifth_lesson = models.CharField('Пятый урок', max_length = 15, default='—', null=True, blank=True)
    fifth_cabinet = models.CharField('Пятый кабинет', max_length = 10, default='—', null = True, blank = True)

    sixth_lesson = models.CharField('Шестой урок', max_length = 15, default='—', null=True, blank=True)
    sixth_cabinet = models.CharField('Шестой кабинет', max_length = 10, default='—', null = True, blank = True)

    seventh_lesson = models.CharField('Седьмой урок', max_length = 15, default='—', null=True, blank=True)
    seventh_cabinet = models.CharField('Седьмой кабинет', max_length = 10, default='—', null = True, blank = True)

    timetable_date = models.DateField('Дата расписания')

    short_lesson = models.BooleanField('Короткие уроки')
    short_break = models.BooleanField('Короткие перемены')
    class Meta: 
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from .models import Timetable, Category



def index(request):
    class_list = Category.objects.all()
    return render(request, 'timetables/list.html', {'class_list':class_list})

# def detail(request, timetable_slug):
#     class_id = Category.objects.filter(slug=timetable_slug)
#     timetables_list = Timetable.objects.filter(class_init=class_id)[:10]
#     return render(request, 'timetables/detail.html', {'timetables_list':timetables_list})

def detail(request, tt_slug):
    try:
        class_id = Category.objects.get(slug = tt_slug)
    except:
        raise Http404("Class not found!")
    # class_id = get_object_or_404(Category, slug = timetable_slug)
    # class_id = Category.objects.get(slug=timetable_slug)

    timetables_list = Timetable.objects.filter(class_init_id=class_id.id)[::-1]
    return render(request, 'timetables/detail.html', {'timetables_list':timetables_list,
    'class_id':class_id})
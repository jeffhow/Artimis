from django.shortcuts import render
from .forms import LessonPlanForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import LessonPlan
from django.views.generic import UpdateView, CreateView

# Landing Page
def index(request):
    return render(request, 'app/index.html')


class LessonPlanUpdate(UpdateView):
    model=LessonPlan
    form_class=LessonPlanForm
   
class LessonPlanCreate(CreateView):
    model=LessonPlan
    form_class=LessonPlanForm
    # fields='__all__'
    
# super generic
from django.views.generic.detail import DetailView
class LessonPlanView(DetailView):
    model=LessonPlan

from .models import Course    
class CourseCreate(CreateView):
    model=Course
    fields='__all__'
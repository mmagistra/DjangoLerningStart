from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from training_site_app.forms import CreateForm
from training_site_app.models import Course


class CoursesRead(ListView):
    model = Course
    context_object_name = 'courses'


class CoursesDetailRead(DetailView):
    model = Course
    context_object_name = 'course'


class CoursesCreatePost(CreateView):
    model = Course
    success_url = reverse_lazy('training_site_app:courses_read')
    form_class = CreateForm


class CoursesUpdate(UpdateView):
    model = Course
    fields = ["name", 'description']
    template_name_suffix = "_update_form"
    success_url = reverse_lazy('training_site_app:courses_read')


class CoursesDelete(DeleteView):
    model = Course
    template_name = 'training_site_app/course_confirm_delete.html'
    success_url = reverse_lazy('training_site_app:courses_read')

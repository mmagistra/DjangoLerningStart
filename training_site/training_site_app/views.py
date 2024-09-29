from django.db.models import Count, QuerySet, Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from training_site_app.forms import CreateForm
from training_site_app.models import Course, Lesson, Student, Educator


class Menu(TemplateView):
    template_name = 'training_site_app/menu.html'


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


class ComplexQueryForStudentsSlow(TemplateView):
    # Для каждого студента нужно показать всех преподавателей, которые его обучают(для каждого его курса)
    template_name = 'training_site_app/complex_query_for_students.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # context['users'] = {{
        #     'user': user,
        #     'educators': []
        # }}
        context['users'] = []

        for user in Student.objects.all():
            record = {'user': user}
            courses: list[Course] = user.studying_on_courses.all()
            courses_names: list[str] = [course.name for course in courses]
            record['educators'] = Educator.objects.filter(
                teaches_courses__name__in=courses_names
            )

            context['users'].append(record)

        return context


class ComplexQueryForStudentsOptimized(TemplateView):
    # Для каждого студента нужно показать всех преподавателей, которые его обучают(для каждого его курса)
    template_name = 'training_site_app/complex_query_for_students_optimized.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        records = Student.objects.prefetch_related(
            'user',
            'studying_on_courses__teachers__user'
        ).all()
        context['records'] = list()
        for record in records:
            educators = []
            for course in record.studying_on_courses.all():
                educators += [teacher.user.username for teacher in course.teachers.all()]
            context['records'].append({
                'user': record.user.username,
                'educators': educators,
            })

        return context


class ComplexQueryForCoursesSlow(TemplateView):
    template_name = 'training_site_app/complex_query_for_courses_slow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        courses: list[Course] = Course.objects.order_by(
            'name'
        ).all()
        context['courses'] = list()

        for course in courses:
            course_data = {
                'name': course.name,
                'students_count': len(course.students.all()),
                'educators_count': len(course.teachers.all()),
                'summary': len(course.students.all()) + len(course.teachers.all()),
            }
            context['courses'].append(course_data)
        return context


class ComplexQueryForCoursesOptimized(TemplateView):
    template_name = 'training_site_app/complex_query_for_courses_slow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        courses: QuerySet[Course] = Course.objects.prefetch_related(
            'teachers',
            'students',
        ).annotate(
            students_count=Count('students', distinct=True),
            educators_count=Count('teachers', distinct=True),
            summary=(Count('students', distinct=True) + Count('teachers', distinct=True)),
        ).order_by(
            'name'
        ).all()
        context['courses'] = courses

        # for course in courses:
        #     course_data = {
        #         'name': course.name,
        #         'students_count': course.stu,
        #         'educators_count': len(course.students.all()),
        #         'summary': len(course.students.all()) + len(course.teachers.all()),
        #     }
        #     context['courses'].append(course_data)
        return context


class ComplexQueryForLessonsSlow(TemplateView):
    template_name = 'training_site_app/complex_query_for_lessons_slow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = []

        courses = Course.objects.all()
        for course in courses:
            if course.lessons.count() >= 2 and any(['Введение' in lesson.name for lesson in course.lessons.all()]):
                context['courses'].append({
                    'name': course.name,
                    'students': course.students.all(),
                })

        return context


class ComplexQueryForLessonsOptimized(TemplateView):
    template_name = 'training_site_app/complex_query_for_lessons_slow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = []

        courses = Course.objects.annotate(
            lessons_count=Count('lessons')
        ).filter(
            Q(lessons__name__icontains='Введение') & Q(lessons_count__gte=2)
        ).prefetch_related(
            'students',
            'students__user'
        ).all()
        for course in courses:
            context['courses'].append({
                'name': course.name,
                'students': course.students.all(),
            })

        return context

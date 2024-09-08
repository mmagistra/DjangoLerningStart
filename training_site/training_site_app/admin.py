import textwrap

from django.contrib import admin

from .models import Course, Lesson, Educator, Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = 'pk', 'username', 'courses'
    list_display_links = 'pk', 'username'
    list_filter = 'user', 'studying_on_courses'

    def username(self, obj: Student) -> str:
        return obj.user

    def courses(self, obj: Student) -> str:
        return ', '.join([course.name for course in obj.studying_on_courses.all()])


@admin.register(Educator)
class EducatorAdmin(admin.ModelAdmin):
    list_display = 'pk', 'username', 'courses'
    list_display_links = 'pk', 'username'
    list_filter = 'user', 'teaches_courses'

    def username(self, obj: Educator) -> str:
        return obj.user

    def courses(self, obj: Educator) -> str:
        return ', '.join([course.name for course in obj.teaches_courses.all()])


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = 'pk', 'number', 'name', 'video', 'short_text', 'course_id'
    list_display_links = 'pk', 'number', 'name', 'video', 'short_text', 'course_id'
    list_filter = ('course_id', )

    def short_text(self, obj: Lesson) -> str:
        return textwrap.shorten(
            obj.text,
            width=50,
            placeholder='...'
        )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'short_description'
    list_display_links = 'pk', 'name'

    def short_description(self, obj: Course) -> str:
        return textwrap.shorten(
            obj.description,
            width=50,
            placeholder='...'
        )

from django.contrib import admin
from django.urls import path

from training_site_app.views import (
    CoursesRead,
    CoursesDetailRead,
    CoursesCreatePost,
    CoursesDelete,
    CoursesUpdate,
    ComplexQueryForStudentsSlow,
    ComplexQueryForStudentsOptimized,
    ComplexQueryForCoursesSlow,
    ComplexQueryForCoursesOptimized,
    ComplexQueryForLessonsSlow, ComplexQueryForLessonsOptimized, Menu,
)


app_name = 'training_site_app'

urlpatterns = [
    path('', Menu.as_view(), name='menu'),
    path('read/', CoursesRead.as_view(), name='courses_read'),
    path('read/<int:pk>/', CoursesDetailRead.as_view(), name='courses_detail_read'),
    path('create/', CoursesCreatePost.as_view(), name='courses_create'),
    path('update/<int:pk>/', CoursesUpdate.as_view(), name='courses_update'),
    path('delete/<int:pk>/', CoursesDelete.as_view(), name='courses_delete'),
    path('queries/1/slow', ComplexQueryForStudentsSlow.as_view(), name='students_query_1_slow'),
    path('queries/1/optimized', ComplexQueryForStudentsOptimized.as_view(), name='students_query_1_optimized'),
    path('queries/2/slow', ComplexQueryForCoursesSlow.as_view(), name='students_query_2_slow'),
    path('queries/2/optimized', ComplexQueryForCoursesOptimized.as_view(), name='students_query_2_optimized'),
    path('queries/3/slow', ComplexQueryForLessonsSlow.as_view(), name='students_query_3_slow'),
    path('queries/3/optimized', ComplexQueryForLessonsOptimized.as_view(), name='students_query_3_optimized'),
]

from django.contrib import admin
from django.urls import path

from training_site_app.views import (
    CoursesRead,
    CoursesDetailRead,
    CoursesCreatePost,
    CoursesDelete,
    CoursesUpdate,
)


app_name = 'training_site_app'

urlpatterns = [
    path('read/', CoursesRead.as_view(), name='courses_read'),
    path('read/<int:pk>/', CoursesDetailRead.as_view(), name='courses_detail_read'),
    path('create/', CoursesCreatePost.as_view(), name='courses_create'),
    path('update/<int:pk>/', CoursesUpdate.as_view(), name='courses_update'),
    path('delete/<int:pk>/', CoursesDelete.as_view(), name='courses_delete'),
]

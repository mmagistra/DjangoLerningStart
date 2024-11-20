from django.urls import path

from frontend.views import TestPage, RequestsCheck

app_name = 'frontend'


urlpatterns = [
    path('test-page/', TestPage.as_view(), name='test-page'),
    path('requests-check/', RequestsCheck.as_view(), name='test-page'),
]

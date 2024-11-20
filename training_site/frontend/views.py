from django.shortcuts import render
from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'frontend/test-page.html'


class RequestsCheck(TemplateView):
    template_name = 'frontend/requests-check.html'

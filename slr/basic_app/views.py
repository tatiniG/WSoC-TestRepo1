from django.shortcuts import render
from django.views.generic import TemplateView

app_name = 'basic_app'


class IndexView(TemplateView):
    template_name = 'basic_app/index.html'


class FrontEndView(TemplateView):
    template_name = 'basic_app/frontend.html'


class BackEndView(TemplateView):
    template_name = 'basic_app/backend.html'
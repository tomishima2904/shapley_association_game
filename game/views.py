from django.shortcuts import render
from django.views import generic


class IndexView(generic.TemplateView):
    template_name = "index.html"


class SignupView(generic.FormView):
    template_name = "signup.html"


class TitleView(generic.TemplateView):
    template_name = "title.html"


class GamingView(generic.TemplateView):
    template_name = "gaming.html"


class ResultsView(generic.TemplateView):
    template_name = "results.html"

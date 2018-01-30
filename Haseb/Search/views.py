# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import VerseForm
from .classSearch import exe


# Create your views here.
class HomeView(TemplateView):
    template_name = 'index.htm'

class AboutPageView(TemplateView):
    template_name = 'about.htm'

class SearchPageView(TemplateView):
    template_name = 'search.htm'
    class PoertyPageView(TemplateView):
        template_name = 'poetry.htm'

class TestPageView(TemplateView):
    template_name = 'testform.htm'



def varse(request):
    form = VerseForm(request.POST or None)

    if form.is_valid():
        for key, value in form.cleaned_data.iteritems():
            print key, value
        print (exe(value))
        d = exe(value)
    context = {
        "form": form,
    }
    return render(request, 'index.htm', context)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.utils.encoding import python_2_unicode_compatible

from .forms import VerseForm
import sqlite3

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


#@python_2_unicode_compatible
def varse(request):
    form = VerseForm(request.POST or None)
    if form.is_valid():
        for key, value in form.cleaned_data.iteritems():
            print key, value
        conn = sqlite3.connect('C://test//myenv//Haseb//db.sqlite3')
        c = conn.cursor()
        c.execute("select text from Search_verse where text like '%"+value+"%';", )
        result = list(c)
        conn.commit()
        for w in result:
            print(w[0])
        conn.close()
    context = {
        "form": form,
    }
    return render(request, 'index.htm', context)

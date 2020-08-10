import json
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _

def index(request):
    ctx = {}
    ctx['title'] = _('Gold price')
    ctx['title'] = _('Hello World')
    return render(request, 'index.html', ctx)

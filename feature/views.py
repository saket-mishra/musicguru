from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Feat, Rockvids, Rockinfo, Genre, Genrevids, Navers, Feedback
from django.template import RequestContext
from django.shortcuts import render_to_response
from django import forms
from .models import ContactForm
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.shortcuts import redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import requests

def rock_and_feat(request):
    feats = Feat.objects.order_by('-created')[:3]
    rocks = Rockinfo.objects.order_by('rank')[:50]
    context = RequestContext(request, {
        'feats': feats, 'rocks': rocks
    })
    return render_to_response('template.html', context)
	
	
	
class DetailView(generic.DetailView):
    model = Feat
    template_name = 'feature/detail.html' 
    context_object_name = 'feat'
	
class RockDetailView(generic.DetailView):
    model = Rockinfo
    template_name = 'feature/detailrock.html' 
    context_object_name = 'rockinfo'
	
class GenreDetailView(generic.DetailView):
    model = Genre
    template_name = 'feature/detailgenre.html' 
    context_object_name = 'genre'

class NaversDetailView(generic.DetailView):
    model = Navers
    template_name = 'feature/detailnaver.html' 
    context_object_name = 'navers'	
	
def about(request):
    context = {'tags': False, 'success': True, 'valid': True}
    return render(request, 'feature/about.html', context)

def contact(request):
    context = {'tags': False, 'success': True, 'valid': True}
    return render(request, 'feature/contact.html', context)

	
def faq(request):
    context = {'tags': False, 'success': True, 'valid': True}
    return render(request, 'feature/faq.html', context)
	
from django.shortcuts import render

def error404(request):
    return render(request,'404.html')

def error500(request):
    return render(request,'500.html')

def feedback(request):
    if 'name' in request.POST and request.POST['name']:
        if 'email' in request.POST and request.POST['email']:
            if 'message' in request.POST and request.POST['message']:
                name = request.POST['name']
                email = request.POST['email']
                message = request.POST['message']
                try:
                    validate_email(email)
                except ValidationError as e:
                    valid = False
                else:
                    valid = True
                f = Feedback(fname = str(name), fmail = email, msg = str(message))
                f.save()
                context = {'tags': True, 'success': True, 'valid': valid}

            else:
                context = {'tags': True, 'success': False, 'valid': True}
        else:
            context = {'tags': True, 'success': False, 'valid': True}
    else:
        context = {'tags': True, 'success': False, 'valid': True}
    return render(request, 'feature/contact.html', context)
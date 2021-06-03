from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from Starehe.settings import EMAIL_HOST_USER
from django.views.generic import TemplateView, ListView
from .models import CAREER, Gallery, Executive, Services
from django.db.models import Q
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def contact(request):
    if request.method == 'POST':
        sender = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['comment']
        recepient = EMAIL_HOST_USER
        send_mail(subject, message, sender, [recepient, sender], fail_silently = False)
        return redirect('/SHCOOL')
    else:
        return render(request, 'SHCOOL/contact.html')

#pppppppppppppppppppp


def Search(request):
    if request.method == 'POST':
        search = CAREER.objects.filter(Q(Title = request.POST['search']) | Q(Description = request.POST['search']))
        return render(request, 'SHCOOL/search_results.html', {'search':search})
    else: 
        return redirect('/SHCOOL') 


#pppppppppppppppppppppp

class OverListView(generic.ListView):
    template_name = 'SHCOOL/Index.html'

    def get_queryset(self):
        return CAREER.objects.all()


#PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
def Gallary(request):
    images = Gallery.objects.all()[:9]
    return render(request, 'SHCOOL/gallery.html', {'images':images})

def About(request):
    executive = Executive.objects.order_by('-pk')[:1]
    return render(request, 'SHCOOL/About.html', {'executive':executive})

# @login_required(login_url='/ACCOUNTS/Login')
def Service(request):    
    servicess = Services.objects.all()[:4]
    return render(request, 'SHCOOL/Services.html', {'services':servicess})

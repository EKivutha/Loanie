from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from client.models import Loan
from accounts.models import person


@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'index'
    def conto(self):
        album = person.objects.all().count()
        return album

    html_template = loader.get_template( 'dashboard.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/dashboard/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
def transactions(request):
        queryset = Loan.objects.all()
        context = {
                "Loan_list":queryset
        }
        return render(request, "transactions.html",context = {"Loan_list":Loan.objects.all})

def users(request):
        queryset = person.objects.all()
        context = {
                "person_list":queryset
        }
        return render(request, "users.html",context = {"person_list":person.objects.all})        
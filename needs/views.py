from bicalca.needs.models import Need
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

def show(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    n = Need.objects.filter(bought = False)
    return render_to_response('needs.html', {'needs' : n, 'logged' : request.user}, context_instance=RequestContext(request))
    
def add(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    return render_to_response('need-add.html', context_instance=RequestContext(request))

def save(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    n = Need(user = request.user,
        caption = request.POST['caption'],
        description = request.POST['description'],
        bought_by=None)
    n.save()
    return HttpResponseRedirect("/hasser")
    
def bought(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    n = Need.objects.get(pk=int(request.GET['id']))
    n.bought = True
    n.bought_by = request.user
    n.save()
    return HttpResponseRedirect("/hasser")

from bicalca.monitor.models import Purchase, Category
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response, get_object_or_404

def show(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    if request.GET.has_key('user'):
        u = request.GET['user']
        if u == 'all':
            p = Purchase.objects.all()
            user = None
        else:
            user = User.objects.get(username=u)
            p = Purchase.objects.filter(user=user)
    else:
        p = Purchase.objects.filter(user=request.user)
        user = request.user
    s = 0
    for o in p:
        s = s + o.cost
    return render_to_response('index.html', {'purchases' : p, 'u': user , 'logged' : request.user, 's' : s}, context_instance=RequestContext(request))

def add(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect("/login/")
    categories = Category.objects.all()
    return render_to_response('add.html', {'categories' : categories}, context_instance=RequestContext(request))
    
def save(request):
    p = Purchase(user = request.user,
        category = Category.objects.get(pk=int(request.POST['category'])),
        caption = request.POST['caption'],
        description = request.POST['description'],
        cost = int(request.POST['cost']))
    p.save()
    return HttpResponseRedirect("/")

def login_first(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/")
    else:
        return render_to_response('login.html', context_instance=RequestContext(request))
    
def log(request):
    firstname = request.POST['username']
    username = User.objects.get(first_name=firstname).username
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            # account is disabled
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
def out(request):
    logout(request)
    return HttpResponseRedirect('/login')

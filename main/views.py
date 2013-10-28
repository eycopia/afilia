from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
#from django.contrib.auth import logout
from django.contrib import auth

@login_required
def index(request):
    request.session["dbse"] = 1
    print type(request.session["dbse"])
    return render_to_response('afiliado/index.html',{},context_instance=RequestContext(request))

@login_required
def redirec_profile(request):	
    return HttpResponseRedirect('/index/')


def login(request):
	if request.POST:
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username, password=password)
		if user is not None and user.is_active:
			auth.login(request, user)
			request.session["dbse"] = "1"
			return HttpResponseRedirect('/index/')
		else:
			return HttpResponseRedirect('/account/invalid/')
	return render_to_response(
		'main/login.html',context_instance=RequestContext(request))
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from ubigeo.models import Ubigeo
from django.core.context_processors import csrf
from django.http import HttpResponse
from django.utils import simplejson


def view_ubigeo(request):
    departamento = Ubigeo.objects.filter(provincia=0, distrito=0)
    return render_to_response('ubigeo/select_ubigeo.html',
        {'ubigeo': departamento}, context_instance=RequestContext(request))


def search_ubigeo(request):
    operar = request.POST.get("operar", "")
    cod = request.POST.get("cod_lugar", "")
    padre = request.POST.get("padre", "")
    
    #preparamos el select
    html = ('<option value="n">-------------</option>')
    
    if operar.upper() == 'PROVINCIA':
        lugares = Ubigeo.objects.filter(
                    departamento=cod, distrito=0).exclude(provincia=0).values()
        for data in lugares:
            html += ('<option value="' + str(data['provincia']) + '">' +
                    data['nombre'] + '</option>')
    else:
        lugares = Ubigeo.objects.filter(provincia=cod,departamento=padre).exclude(distrito=0).values()
        for data in lugares:
            html += ('<option value="' + str(data['distrito']) + '">' + 
                    data['nombre'] + '</option>')
   
    return HttpResponse(simplejson.dumps(html), mimetype='application/json')
# -*- coding: utf8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.db import transaction
from django.db.models import Q
from django.utils import simplejson
from django.core  import  serializers
#cargamos todos los modelos de este app
from afiliado.models import *
from forms import AfiliadoForm
from ubigeo.models import Ubigeo
from datetime import date


#se deben mostrar todos aquellos que pagaron por un carnet
@login_required
@login_required
def search_afiliado(request):
    if 'q' in request.GET:
        q = request.GET['q']
        s_list = Afiliado.objects.filter(
                          Q(nombres__icontains=q) | Q(apellidos__icontains=q)
                          | Q(dni__icontains=q))
    else:
        s_list = Afiliado.objects.all()[:75]

    paginator = Paginator(s_list,14)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return render_to_response('afiliado/search-afiliado.html',
        {'afiliado' : data}, context_instance=RequestContext(request))


@login_required
@transaction.commit_on_success
def add_afiliado(request):
    formAfiliado = AfiliadoForm(request.POST or None)

    if formAfiliado.is_valid():

        base = Base.objects.get(pk=int(request.POST.get('base')))

        formAfiliado = formAfiliado.save(commit=False)
        formAfiliado.correlativo = base.correlativo + 1
        base.correlativo = base.correlativo + 1
        base.save()

        formAfiliado.save()

        iafiliado = Afiliado.objects.latest('id')


        #Insertar Familiares
        num_fam = int(request.POST.get('num_fam'))
        for i in range(num_fam):
            tipo_fam = Tipo_Familiar.objects.get(id=request.POST[("tipo_fam%d" % i)])
            sex_fam = int(request.POST[("sex%d" % i)])
            familiar = Familiar(
                afiliado=iafiliado,
                tipo_familiar=tipo_fam,
                nombres=request.POST[("fam%d" % i)],
                edad=request.POST[("edad%d" % i)],
                sexo=sex_fam)
            familiar.save()
        return HttpResponseRedirect('/')
    else:
        print formAfiliado.errors
    #extraemos los departamentos de Ubigeo
    departamento = Ubigeo.objects.filter(provincia=0, distrito=0)
    #cargamos tipos de familiares
    t_familiar = Tipo_Familiar.objects.all()

    #extraemos el último Afiliado registrado
    try:
        iafiliado = Afiliado.objects.latest('id')
        id_afiliado = iafiliado.id + 1
    except Afiliado.DoesNotExist:
        id_afiliado = 1

    return render_to_response('afiliado/frm_new_afiliado.html',
            {'form': formAfiliado, 'cod_afiliado': id_afiliado,
            'departamento': departamento, 'familiar':t_familiar },
            context_instance=RequestContext(request))


def reporte_datos_afiliados(request):
    afiliado = Afiliado.objects.all()
    return render_to_response('afiliado/reporte_datos_afiliado.html',
        {'afiliados':afiliado}, context_instance=RequestContext(request))

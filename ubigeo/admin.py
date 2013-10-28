from django.contrib import admin

from ubigeo.models import Ubigeo

class UbigeoAdmin(admin.ModelAdmin):
	list_display = ('id','departamento','provincia','distrito','nombre')
	search_fields = ['nombre']


admin.site.register(Ubigeo,UbigeoAdmin)
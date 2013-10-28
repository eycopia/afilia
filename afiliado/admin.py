#encoding:utf-8
from django.contrib import admin

from afiliado.models import (Afiliado,  Categoria, Instruccion,
Tipo_Vivienda, Especialidad, Tipo_Familiar, Familiar, Base)


class AfiliadoAdmin(admin.ModelAdmin):
	#Retorna nombres y apellidos concatenado en mayuscula
	def nombre_afiliado(Afiliado):
		return '<span style="color: #%s;font-weight:bold">%s %s</span>' % ('000000', Afiliado.nombres, Afiliado.apellidos)

	nombre_afiliado.short_description = 'Nombres'
	nombre_afiliado.allow_tags = True

	#personalizacion de datos para la administración
	fieldsets = (
		('Datos Básicos', {
				'fields' : (('id','correlativo','fecha_inscripcion'),('nombres', 'apellidos'),
					('dni', 'telefono'),('cuspp','essalud'),'base')
		}),
		('Residencia', {
			'classes':('collapse','wide','extrapretty'),#otros son: wide, extrapretty
			'fields': (('lugar_nacimiento','fecha_nacimiento'),('residencia',
				'direccion'),'tipo_vivienda')
		}),
		('Otros Datos', {
			'classes':('collapse',),
			'fields' : ('estado_civil',('sexo', 'estado'),('categoria',
				'especialidad'),'instruccion')
		}),
	)

	actions_on_top = False
	actions_selection_counter = False
	#admin.site.disable_action('delete_selected')

	# tambien puede ir un metodo como: upper_case_name, decade_born_in
	list_display = ('id','correlativo','dni',nombre_afiliado,'categoria','fecha_inscripcion','base')

	#sirve para mostrar links al objeto
	list_display_links = ('id',nombre_afiliado,)

	list_filter = ('fecha_inscripcion','categoria','especialidad')

	#decimos que campos pueden ser editables desde la grilla
	list_editable = ('correlativo',)

	#cantidad de registro al mostrar todo
	#list_max_show_all = 5

	#registros por página
	list_per_page = 25

	#se supone que me da las relaciones tipo foreignkey
	list_select_related = True

	#modo de orden
	ordering = ['-id']

	#indicamos cuales seran radio buttons
	radio_fields = {'sexo':admin.VERTICAL,'estado':admin.VERTICAL}

	#te muestra el id del campo relacionado, para que asignes el valor
	raw_id_fields = ('categoria','lugar_nacimiento','residencia')

	#muestra el campo, sin opcion a editar
	readonly_fields = ('id',)

	#coloca, los botones de guardar en la parte superior del formulario
	#save_on_top = True

	search_fields = ['nombres','^apellidos','dni','id']

class CarnetAdmin(admin.ModelAdmin):
	list_display = ('id','afiliado','fecha_emision','fecha_vencimiento')
	list_filter = ('tipo_operacion',)
	raw_id_fields = ('afiliado',)

class FamiliarAdmin(admin.ModelAdmin):

	list_display = ('nombres','afiliado','tipo_familiar')

	search_fields = ['afiliado__nombres','afiliado__apellidos','nombres']

	list_display_links = ('nombres',)



class BaseAdmin(admin.ModelAdmin):
	raw_id_fields = ('distrito',)


admin.site.register(Afiliado, AfiliadoAdmin)
admin.site.register(Base, BaseAdmin)
admin.site.register(Categoria)
admin.site.register(Instruccion)
admin.site.register(Tipo_Vivienda)
admin.site.register(Especialidad)
admin.site.register(Tipo_Familiar)
admin.site.register(Familiar, FamiliarAdmin)
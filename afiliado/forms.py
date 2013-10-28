#encoding:utf-8
from django import forms
from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, CheckboxInput
from afiliado.models import Tipo_Vivienda, Afiliado
from django.forms import ModelForm


class AfiliadoForm(ModelForm):

    class Meta:
        exclude = ('correlativo')
        model = Afiliado
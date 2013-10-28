jQuery.fn.reset = function () {
  $(this).each (function() { this.reset(); });
}

$(function(){
    $("#formulario").reset();
})

$(function(){
    $('#num_emp').val('0');
    $('#num_fam').val('0');

    // Datepicker
    $('.form_date').datepicker({
                    changeMonth: true,
                    changeYear: true,
                    regional:'es',
                    yearRange: "1930:",
                    dateFormat: "dd/mm/yy"
    });

    /*Carga de los ubigeos*/
    $departamento = 0;
    $('.departamento').change(function(){
        $departamento = $(this).val();
        procesar($(this).val(),"provincia", $(this).attr('rel'),0);
    });

    $('.provincia').change(function(){
        procesar($(this).val(),"distrito", $(this).attr('rel'),$departamento);
    });

    /*
    * idSelect, id del select padre
    * operar, buscara los lugares que tenga este dato
    * selec, select a modificar
    */
    function procesar(idSelect,operar,select,padre){
        $.ajax(
                {
                    type: 'POST',
                    url: '/ubigeo/',
                    data: 'cod_lugar='+idSelect+'&operar='+operar+'&padre='+padre,
                    success: function(resp){
                        $('#'+select).attr('disabled',false).html(resp);
                    }
                }
                );
        }
    /**********************/

    /*Agrega campos a tabla de familiares */
    var num_reg = 1;
    $('#add_reg').click(function(){
        var tip_fam = $('#tipo_fam1').clone();
        tip_fam.attr('name','tipo_fam'+num_reg);
        tip_fam.attr('id','');
        //preparamos el nuevo registro
        html = '<tr><td><input type="text" class="large" name="fam'+num_reg+'">';
        html += '</td><td><input type="text" name="edad'+num_reg+'" class="peq"></td></td>';
        html += '<td><input type="radio" value="0" name="sex'+num_reg+'" class="peq"> Varon';
        html += '<input type="radio" value="1" name="sex'+num_reg+'" class="peq"> Mujer</td>';
        html +='<td id="sel_fam'+num_reg+'"></td></tr>';
        //agregamos el generado
        $('#familiares tbody').append(html);
        //agregamos dentro del anterior el select
        $('#sel_fam'+num_reg).append(tip_fam);
        num_reg++
        $('#num_fam').val(num_reg);
    });
    /*************************************************/

});

/********************* Validar Formulario *************************************/
$(function(){
$("#formulario").validate({
    rules: {
            fecha_inscripcion: {
                required: true
            },
            nombres:"required",
            apellidos:"required",
            dni:{
                required:true,
                minlength: 8,
                maxlength: 8

            },
            telefono: {
                minlength: 6,
                maxlength: 11
            },
            sexo: "required",
            fecha_nacimiento:"required",
            lugar_nacimiento:"required",
            residencia:"required",
            tipo_vivienda:"required",
            categoria:"required",
            especialidad:"required",
            instruccion:"required"

    },
    messages: {
                fecha_inscripcion: "Ingrese la Fecha de Afiliación"
    }
 });
})
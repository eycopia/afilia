$(function(){
  // Datepicker
  $('.form_date').datepicker({
  changeMonth: true,
  changeYear: true,
  monthNames: ["Enero","Febrero","Marzo","Abril","May","Junio","Julio","Agosto","Setiembre","Octubre","Noviembre","Deciembre"],
    yearRange: "1930:",
    dateFormat: "dd/mm/yy"
  });
});

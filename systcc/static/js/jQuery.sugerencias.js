(function($){
	$.fn.sugerencias = function(opciones) {
		
		var
		  defecto = {
		  	background: ' #fbf289',
			color: '#003',
			rounded: false
		  },
		  settings = $.extend({}, defecto, opciones);
		  
		  this.each(function() {
		  	var $this = $(this);
			var titulo = this.title;
			
			if($this.is('input') && $this.attr('title') != '') {
				this.title = '';
				$this.hover(function(e) {
					// rat�n over
					$('<div id="sugerencias" />')
					  .appendTo('body')
					  .text(titulo)
					  .hide()
					  .css({
					  	backgroundColor: settings.background,
						color: settings.color,
						top: e.pageY + 10,
						left: e.pageX + 20
					  })
					  .fadeIn(350);
					  
				  if(settings.rounded) {
				  	$('#sugerencias').addClass('rounded');
				  }
				}, function() {
					// rat�n out
					$('#sugerencias').remove();
				});	
			}
			
			$this.mousemove(function(e) {
				$('#sugerencias').css({
					top: e.pageY + 10,
					left: e.pageX + 20
			     });
			});
			
		  });
		  // devolvemos el objeto jQuery para permitir su uso en cadena.
		  return this;
	}
})(jQuery);

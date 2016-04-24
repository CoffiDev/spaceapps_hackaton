$(document).ready(function(){
	var estado = false;

	$('#btn-toggle').on('click',function(){
		$('.seccionToggle').slideToggle();

		if (estado == true) {
			$(this).text("CanSat AirChecker");
			$('body').css({
				"overflow": "auto"
			});
			estado = false;
		} else {
			$(this).text("Volver a Air Checker ");
			$('body').css({
				"overflow": "hidden"
			});
			estado = true;
		}
	});
});
window.Superlists = {};
window.Superlists.initialize  = function initialize() {
	$('input[name="text"]').on('keypress', function(){
		$('.has-error').hide();
	});
}
$(function() {

	$("#slider").draggable({
		axis: 'x',
		containment: 'parent',
		drag: function(event, ui) {
			if (ui.position.left > 200) {
				$("#well").fadeTo(2000, 0);
				$("#watchpoint").fadeOut(2000);
				$("#sec").fadeOut(2000);
				$("#hour").fadeOut(2000);
				$("#min").fadeOut(2000);
				$(".clock-menu-lists").fadeIn(3000);
			} else {
				$(".unlock-content span").css("opacity", 100 - (ui.position.left / 5))
			}
		},
		stop: function(event, ui) {
			if (ui.position.left < 200) {
				$(this).animate({
					left: 0
				})
			}
		}
	});

	// The following credit: http://www.evanblack.com/blog/touch-slide-to-unlock/

	$('#slider')[0].addEventListener('touchmove', function(event) {
	    event.preventDefault();
	    var el = event.target;
	    var touch = event.touches[0];
	    curX = touch.pageX - this.offsetLeft - 73;
	    if(curX <= 0) return;
	    if(curX > 200){
	    	$('#well').fadeOut();
	    }
	   	el.style.webkitTransform = 'translateX(' + curX + 'px)';
	}, false);

	$('#slider')[0].addEventListener('touchend', function(event) {
	    this.style.webkitTransition = '-webkit-transform 0.3s ease-in';
	    this.addEventListener( 'webkitTransitionEnd', function( event ) { this.style.webkitTransition = 'none'; }, false );
	    this.style.webkitTransform = 'translateX(0px)';
	}, false);

});
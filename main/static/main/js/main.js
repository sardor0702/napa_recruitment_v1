$(document).ready(function(){
	$(window).scroll(function(){
        if(this.scrollY > 200){
            $('.scroll-up-btn').addClass("show");
        }else{
            $('.scroll-up-btn').removeClass("show");
        }
  });

	$('.scroll-up-btn').click(function(){
		$('html').animate({scrollTop: 0});
	});
});

$(".checkbox-menu").on("change", "input[type='checkbox']", function() {
   $(this).closest("li").toggleClass("active", this.checked);
});

$(document).on('click', '.allow-focus', function (e) {
  e.stopPropagation();
});

$(".favourite-icon").click(function(){
	clicked = true;
	if (clicked) {
		$(this).toggleClass('active');
		clicked = true;
	}else{
		$(this).removeClass('active');
		clicked = false;
	}
});

$(".favourite-icon-1").click(function(){
	clicked = true;
	if (clicked) {
		$(this).toggleClass('active');
		clicked = true;
	}else{
		$(this).removeClass('active');
		clicked = false;
	}
});
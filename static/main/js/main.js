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


const inpFile = document.getElementById("inpFile");
const previewContainer = document.getElementById("imagePreview");
const previewImage = previewContainer.querySelector(".image-preview__image");
const previewDefaultText = previewContainer.querySelector(".image-preview__default-text");


inpFile.addEventListener("change", function(){
	const file = this.files[0];


	if (file) {
		const reader = new FileReader();

		previewDefaultText.style.display = "none";
		previewImage.style.display = "block";

		reader.addEventListener("load", function(){
			previewImage.setAttribute("src", this.result);
		});

		reader.readAsDataURL(file);
	}else{
		previewDefaultText.style.display = null;
		previewImage.style.display = null;
		previewImage.setAttribute("src", "");
	}
});




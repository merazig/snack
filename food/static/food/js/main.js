AOS.init({
    duration: 1200
});

$(document).ready(function(){
    $(window).scroll(function(){
         var scroll = $(window).scrollTop();
         if(scroll > 100){
             $("#mynav").css("background-image", "linear-gradient(45deg, rgb(5, 143, 74, 95), rgb(3, 63, 40, 0.95))");
         }
         else{
             $("#mynav").css("background-image", "linear-gradient(45deg, rgb(5, 143, 74, 0.4), rgb(3, 63, 40, 0.4))");
         }
    })
})
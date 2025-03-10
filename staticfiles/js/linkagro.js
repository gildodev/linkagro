// Carregamento de pagina

$(document).ready(function () {
    
    setTimeout(function () {
        $('.drawer').addClass('open');
        document.querySelector('.empty-msg').style.opacity = 1;
    }, 500);

    let navbar = $("#navbar");
        let subnav = $("#show-only-scroll-down");
        let area_pesquisa = $("#area-pesquisa");
        let area_navegacao = $("#area-navegacao");
        let area_pesquisa_btn = $("#btn-search-close");
        let area_pesquisa_btn_close = $("#navbar-btn-closed");
        let menu_navegacao=$("#menu-navegacao-mobile");
        let btn_pesquisar=$("#btn-pesquisar");
        let btn_close_menu=$("#btn-close-menu");
        let abrir_menu = $("#abrir-menu");
        let navbarHeight = navbar.outerHeight() + 30;
        let verificar_se_clicou_btn_pesquisa=true;
        let verificar_se_clicou_abrir_menu=true;


        $(window).on("scroll", function () {

            if ($(this).scrollTop() > navbarHeight) {
                navbar.addClass("fixed-top")
                navbar.removeClass("sticky-top") 
            } else {
                navbar.addClass("sticky-top") 
                navbar.removeClass("fixed-top")
            }
        });

        $(area_pesquisa_btn).on("click", function () {

            if (verificar_se_clicou_btn_pesquisa) {
                area_navegacao.addClass("animate__slideInDown")
                area_pesquisa.addClass("active animate__slideInDown");
                area_pesquisa_btn.addClass("active")
                verificar_se_clicou_btn_pesquisa=false;
            } else {
                
                area_pesquisa.removeClass("active animate__slideInUp ")
                area_navegacao.addClass("animate__slideInDown")
                area_pesquisa_btn.removeClass("active")
                verificar_se_clicou_btn_pesquisa=true;
            }
            
        });

        $(area_pesquisa_btn_close).on("click", function () {

            if (verificar_se_clicou_btn_pesquisa) {
                area_navegacao.addClass("animate__slideInDown")
                area_pesquisa.addClass("active animate__slideInDown");

                verificar_se_clicou_btn_pesquisa=false;
            } else {
                
                area_pesquisa.removeClass("active animate__slideInUp ")
                area_navegacao.addClass("animate__slideInDown")
                verificar_se_clicou_btn_pesquisa=true;
            }

        });

        // Abrir menu
        $(abrir_menu).on("click", function () {

            if (verificar_se_clicou_abrir_menu) {
                abrir_menu.addClass("active")
                menu_navegacao.removeClass("animate__fadeOutLeft")
                menu_navegacao.addClass("active animate__fadeInLeftBig")
                verificar_se_clicou_abrir_menu=false;
            }
        });
        
        $(btn_close_menu).on("click", function () {

            if (!verificar_se_clicou_abrir_menu) {
                
                abrir_menu.removeClass("active")
                menu_navegacao.addClass("animate__fadeOutLeft")
                verificar_se_clicou_abrir_menu=true;
            }
        });


    /*---brand container activation---*/
    var $brandContainer = $('.brand_container');
    if($brandContainer.length > 0){
        $('.brand_container').on('changed.owl.carousel initialized.owl.carousel', function (event) {
            $(event.target).find('.owl-item').removeClass('last').eq(event.item.index + event.page.size - 1).addClass('last')}).owlCarousel({
            loop: true,
            nav: false,
            autoplay: false,
            autoplayTimeout: 8000,
            items: 5,
            margin: 20,
            dots:false,
            responsiveClass:true,
            responsive:{
                    0:{
                    items:1,
                },
                300:{
                    items:2,
                    margin: 15,
                },
                480:{
                    items:3,
                },
                768:{
                    items:4,
                },
                992:{
                    items:5,
                },

            }
        });
    }


    $('#loading-page').toggleClass('active');
})
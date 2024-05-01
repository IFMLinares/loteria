var VideoManager = (function() {
    // Método privado
    function onVideoEnd() {
        console.log('Video ended');
        $('#carouselExampleFade').carousel('next');
    }

    function onSlide(event) {
        var activeSlide = $(event.relatedTarget);
        if (activeSlide.attr('id') === 'video_1' || activeSlide.attr('id') === 'video_2' || activeSlide.attr('id') === 'video_3' ) {
            if(activeSlide.attr('id') === 'video_1'){
                var videoElement = $('#video_promo_1');
            }else if(activeSlide.attr('id') === 'video_2'){
                var videoElement = $('#video_promo_2');
            }else{
                var videoElement = $('#video_promo_3');
            }
            if (videoElement.length > 0) {
                videoElement[0].currentTime = 0; // Reinicia el video
                videoElement[0].play(); // Reproduce el video
            }
        }
    }

    // Métodos públicos
    return {
        iniciar: function() {
            $('#video_promo').on('ended', onVideoEnd); // Cambia '#video_1 video' por '#video_promo'
            $('#carouselExampleFade').on('slid.bs.carousel', onSlide);
        }
    };
})();

// Uso del objeto
VideoManager.iniciar();
